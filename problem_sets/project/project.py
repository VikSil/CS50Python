import re
import openpyxl
import requests
import pandas as pd
import advertisements as ads

from random import randint
from bs4 import BeautifulSoup

# --------------------------------------------------------
# == GLOBAL VARIABLES ==
# --------------------------------------------------------

# the root of the website, prefix for all other urls
root_url = "https://www.ss.lv"

# flag whether to save HTML files to disk
saveads = False

# --------------------------------------------------------
# == CUSTOM EXCEPTION CLASS ==
# --------------------------------------------------------

class UnsuportedAdType(Exception):
    "Raised for Ad types 2, 4 and 5"
    pass

# --------------------------------------------------------
# == MAIN FUNCTION ==
# --------------------------------------------------------


def main():
    # This will be a list of advertisement.Flat objects!!!
    adlist = []

    # all parsed BeautifulSoup objects prefixed with "p"
    proot = req_and_save(root_url, "mainpage.html")

    # the landing page will be kept in this data structure
    main_tree_dict = make_main_tree(proot)
    # listify the main landing page for user prompt
    main_tree_list = tree_to_list(main_tree_dict)

    # prompt user for category to download - only accepts Real Estate - Flats for CS50P final project
    cat = prompt_input(main_tree_list)
    i, j = extract_cats(cat)
    url_ext = main_tree_list[i][j][0][1]
    url = root_url + url_ext

    # request all regions where Flats are advertised
    pall_flats = req_and_save(url, "flats.html")
    # listify Flat advertisement regions for user prompt
    all_regions = listify_dict(get_all_links(pall_flats, "h4"))

    # promt user for region to download, zero for all regions, or a number for a specific region
    # this could be improved to accept multiple region prompts
    region = prompt_region(all_regions)
    # gets the name of the output file
    outputfile = input("Please input the name of the output file: ")
    if len(outputfile) < 1:
        outputfile = "output"
    if not outputfile.endswith("xlsx"):
        outputfile = outputfile + ".xlsx"

    print("Thank you. Data is being prepared...")

    # iterates through regions
    url_ext = []
    if region == 0:
        # iterates through all ads user input zero - takes a long time with 7000+ requests
        [url_ext.append(v[1]) for v in all_regions[:-1]]
    else:
        url_ext.append(all_regions[region - 1][1])

    # iterates through region URLs
    for urls in url_ext:
        url = root_url + urls
        ppage = req_and_save(url, get_savename(url))

        # regions with less than 200 ads will show a listing of ads
        # regions with more than 200 ads will have an intermediary page divided by parishes
        # if region page not a listing of ads, then need to parse one level deeper
        if not is_listing_page(ppage):
            # finds all links on the region page
            all_sublinks = get_all_links(ppage, "h4")
            # looks for link that points to a page with all ads for the region
            url = root_url + all_sublinks["Visi sludinājumi"]
            ppage = req_and_save(url, get_savename(url))

        # finds all links to individual ads on all tabs/pages of a listing
        ads = parse_listing_page(ppage, url)

        # for each ad scrapes all the ad data
        for i in ads:
            try:
                adlist.append(scrape_ad(i))
            except UnsuportedAdType:
                continue

        # output one listing dataframe at a time - file remains open and is upended while inside the session
        output_to_excel(adlist, outputfile)
        print(
            "Finished downloading ads for:",
            urls.split("/")[-2].replace("-", " ").capitalize(),
        )


# --------------------------------------------------------
# == END OF MAIN FUNCTION ==
# --------------------------------------------------------

# --------------------------------------------------------
# == STRUCTURAL FUNCTIONS ==
# --------------------------------------------------------


# outputs a list of ads to Excel
def output_to_excel(adlist: list, out_file_name: str):
    all_rows = []

    for ad in adlist:
        row = ad.listmyself()
        all_rows.append(row)

    df = pd.DataFrame(all_rows)
    headers = [
        "URL",
        "AD TYPE",
        "PRICE",
        "CCY",
        "FRACTIONAL PRICE",
        "FRACTION",
        "AREA",
        "ROOMS",
        "CITY",
        "PARISH",
        "VILLAGE",
        "STREET",
        "LEVEL",
        "BUILDING ERA",
        "BUILDING TYPE",
        "DESCRIPTION",
    ]

    with pd.ExcelWriter(out_file_name, engine="openpyxl") as writer:
        df.to_excel(writer, "Sheet1", index=False, header=headers)

    return None


# --------------------------------------------------------


# takes a URL of an individual ad and returns an Ad.Flat object with data as properties
def scrape_ad(url):
    print("scraping url:", url)

    # this will be unpacked as kwargs to Ad.Flat object init
    attributes = {}

    # pull down the ad
    padpage = req_and_save(url, get_savename(url))

    # find advertisement type
    adtype = padpage.find("h2", {"class": "headtitle"}).text.split("/")[-1].strip()
    match adtype:
        case "Pārdod":
            adtype_num = 1
        case "Pērk":
            adtype_num = 2
        case "Izīrē":
            adtype_num = 3
        case "Īrē":
            adtype_num = 4
        case _:
            adtype_num = 5

    # raise exception for ads with irregular data (swap, barter and alike), buy and rent in
    # these usually don't have parsable information in the HTML tags
    if adtype_num == 5 or adtype_num == 4 or adtype_num == 2:
        raise UnsuportedAdType

    # find the price, ccy, fractional price and area/period of the fraction
    long_price = padpage.find("td", class_="ads_price").get_text().strip()
    bracket = long_price.find("(")
    baseprice, ccy = pricesplit(long_price[: bracket - 1])
    fractprice, fract = pricesplit(long_price[bracket + 1 : -1])

    # find data specific to the Ad.Flat
    nested_table = padpage.find("table", {"class": "options_list"}).find_all("table")
    cells = [
        el
        for sublist in [tr.findChildren("tr", recursive=False) for tr in nested_table]
        for el in sublist
    ]
    for cell in cells:
        opt_name = cell.find("td", {"class": "ads_opt_name"}).text.strip()
        opt = cell.find("td", {"class": "ads_opt"}).text.strip()

        match opt_name:
            case "Pilsēta, rajons:":
                city = opt
            case "Pilsēta:":
                city = opt
            case "Pilsēta/pagasts:":
                attributes["parish"] = str(opt)
            case "Ciems:":
                attributes["village"] = str(opt)
            case "Rajons:":
                attributes["village"] = str(opt)
            case "Iela:":
                bracket = opt.find("[")
                opt = opt[: bracket - 1].strip()
                attributes["street"] = str(opt)
            #the site allows for unspecified number of rooms
            case "Istabas:":
                try:
                    rooms = int(opt)
                except:
                    rooms = 0
            case "Platība:":
                area = opt
            case "Stāvs:":
                attributes["level"] = str(opt)
            case "Sērija:":
                attributes["series"] = str(opt)
            case "Mājas tips:":
                attributes["buildingtype"] = str(opt)

        #it is possible to place an ad without specifying a city
        try:
            if len(city)>0:
                continue
        except:
            city = url.split("/")[-2].replace("-", " ").capitalize()

    # find the description of the ad
    desc = padpage.find("div", {"id": "msg_div_msg"})
    # finds all text in the tag. There is probably a better way to do this, i.e. to remove table sub-tag and then extract text
    # but I could not find how to do it without interfering with extracting other data - room for improvement
    text = desc.find_all(string=True, recursive=True)

    # parse through the text to consolidate the relevant lines only
    new_text = []
    [new_text.append(t.replace("\n", "").strip()) for t in text if t != "\n"]
    index = [new_text.index(el) for el in new_text if el.startswith("Pilsēta")][0]
    descript = ""

    for i in range(len(new_text[:index])):
        descript = descript + " " + new_text[i]
    descript.strip()

    # creates an Ad.Flats object and initialises properties with data from the ad
    ad = ads.Flat(
        url,
        adtype_num,
        baseprice,
        ccy,
        descript,
        city,
        area,
        rooms,
        fractprice,
        fract,
        **attributes,
    )

    return ad


# --------------------------------------------------------


# takes a URL of an ad listing, parses through all tabs/pages and returns a set of all URLs to individual ads
def parse_listing_page(ppage, url):
    # contains all links to tabs/pages and a flag whether the tab/page has been parsed yet
    pagelist = {url: False}
    end_links = {}

    # if valid url
    while len(url) > 1:
        # ads tabs/pages that were not previously visible to the tab/page list
        refresh_pagelist(pagelist, ppage)
        # gets all URLs to individual ads on the current tab/page
        end_links.update(get_all_links(ppage, "div.d1"))
        # marks this tab/page as parsed
        pagelist[url] = True
        # check if there are any yet unparsed tabs/pages in the list and repeats the loop
        try:
            url = [k for k in pagelist if pagelist[k] == False][0]
            # this request will fail when all tabs/pages are parsed because url will be None type object
            ppage = req_and_save(url, get_savename(url))
        except:
            # if all tabs/pages have been parsed, then break out of the loop
            url = ""

    # converts values from the individual ad URL dictionary to a set or URLs to avoid duplicates
    end_links_set = strip_values(end_links)

    return end_links_set


# --------------------------------------------------------


# ads tabs/pages currently visible on a listing to a dictionary
# works without return (not sure why, maybe because it is a BeautifulSoup object??)
def refresh_pagelist(pagelist: dict, ppage):
    nav_links = get_all_links(ppage, "div.td2")
    for v in nav_links:
        nav_links[v] = add_root(nav_links[v])
        if nav_links[v] not in pagelist:
            # if new then add to tab/page dictionary and set flag that it has not been parsed before
            pagelist[nav_links[v]] = False


# --------------------------------------------------------
# == END OF STRUCTURAL FUNCTIONS ==
# --------------------------------------------------------

# --------------------------------------------------------
# == SPLITTERS, CONCATENATORS ==
# --------------------------------------------------------


# splits price number and ccy in separate variables
def pricesplit(priceccy: str):
    price, ccy = priceccy.split(" €")
    price = float(price.replace(" ", ""))
    ccy = "EUR" + ccy
    return price, ccy


# makes a callable URL
def add_root(url: str):
    return root_url + url


# extracts categories from user input
def extract_cats(cat):
    cat1, cat2 = cat.split("-")
    return int(cat1) - 1, int(cat2)


# --------------------------------------------------------
# == CONVERTORS ==
# --------------------------------------------------------


# returns all values from a dictionary as a set
def strip_values(dict):
    valueset = set()
    {valueset.add(add_root(dict[k])) for k in dict}

    return valueset


# --------------------------------------------------------


# returns a dict as a list of tuples
def listify_dict(dict):
    return [(k, v) for k, v in dict.items()]


# --------------------------------------------------------


# returns the main tree as a list for enumeration
def tree_to_list(tree: dict):
    tree_list = []
    for k in tree:
        tree_sublist = []
        tree_sublist.append(k)
        tree_sublist.append(listify_dict(tree[k]))
        tree_list.append(tree_sublist)
    return tree_list


# --------------------------------------------------------


# takes the landing page and returns URLs as a tree of dicts
def make_main_tree(ppage):
    tree = {}

    # go through all H2 headers
    sections = ppage.find_all("div", {"id": "main_img_div"})

    for i in range(len(sections)):
        h2 = sections[i].find("h2")

        # get the href and title of the H2 header in a dict
        dict_h2 = get_all_links(h2, "h2")

        # convert it to tuple because dictionaries do not allow nested dictionaries as keys
        tuple = [(k, v) for k, v in dict_h2.items()][0]

        # get all the main category links that can be probed into
        main_cats = get_all_links(sections[i], "div.main_category")

        # add the tuple as key to landing page data structure
        tree[tuple] = main_cats

    return tree


# --------------------------------------------------------
# == END OF CONVERTORS ==
# --------------------------------------------------------

# --------------------------------------------------------
# == OTHER HELPER FUNCTIONS ==
# --------------------------------------------------------


# implies the name of a page to save from the URL
# on failure returns a random name
def get_savename(url):
    try:
        splices = url.split("/")

        if splices[-1].endswith(".html"):
            return splices[-2] + "." + splices[-1]
        else:
            return splices[-2] + "." + splices[-1] + ".html"
    except:
        return "Random_pagename_" + str(randint(1, 1000000)) + ".html"


# --------------------------------------------------------


# finds all links in given tag type (has to be sub-tag to ppage)
def get_all_links(ppage, tagtype):
    searchstr = str(tagtype) + " a"
    hrefs = ppage.select(searchstr)
    dict = {href.text.strip(): href["href"] for href in hrefs}

    return dict


# --------------------------------------------------------


# returns and optionaly saves a web page
def req_and_save(url, *args):
    # pull HTML from the Web
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")

    # save to a file if page name is given and saving is enabled globally
    if len(args) == 1 and saveads:
        with open(args[0], "w") as file:
            file.write(doc.prettify())

    return doc


# --------------------------------------------------------


# load HTML from file and return as parsed object
def read_html(filename):
    with open(filename, "r") as html_file:
        return BeautifulSoup(html_file, "html.parser")


# --------------------------------------------------------


# checks if a page is a listing of ads
def is_listing_page(ppage):
    noindex = ppage.find("noindex")
    if noindex:
        return True
    return False


# --------------------------------------------------------


# prints a list with enumeration
def output_list(somelist: list):
    for i, el in enumerate(somelist):
        print(str(i + 1), "-", somelist[i][0])


# --------------------------------------------------------


# prints main tree with enumeration
def output_tree(tree: list):
    for i, el in enumerate(tree):
        print(str(i + 1), "-", tree[i][0][0])
        for j, subel in enumerate(el[1]):
            print("    ", str(j + 1), "-", subel[0])


# --------------------------------------------------------
# == END OF HELPER FUNCTIONS ==
# --------------------------------------------------------

# --------------------------------------------------------
# == USER PROMPTS ==
# --------------------------------------------------------


# First dialog with the user - prompts for the category of ads to download
# Only accepts "3-1" for Real Estate - Flats for the purposes of CS50P final project
def prompt_input(main_tree_list):
    print(
        "This python program is a web scraper. It downloads real-estate market data from Latvia's main advertising site www.ss.lv"
    )
    print(
        "When prompted input the category that you want to download the data for in form X-Y"
    )
    print(
        "For CS50P final project only Real Estate - Flats data can be downloaded. Please input: 3-1"
    )
    input("Press Enter to see all categories on www.ss.lv")
    print()
    output_tree(main_tree_list)

    while True:
        cat = input("Please input category code ")
        pattern = re.search(r"^[1-9]{1}[0-2]*-[1-9]{1}[0-2]*$", cat)
        if pattern:
            match cat:
                case "3-1":
                    # ONCE FINISHED, PUT THE CODE HERE
                    break
                case _:
                    print(
                        "For CS50P final project only Real Estate - Flats data can be downloaded. Please input: 3-1"
                    )
        else:
            print("Invalid format. Please input: 3-1")

    return cat


# --------------------------------------------------------


# Second dialog with the user - prompts for the region to download ads for
def prompt_region(all_regions):
    print("\nThese are the regions of Latvia:")
    output_list(all_regions)
    print("\nPlease type the number of the region you are interested in.")
    print("\nAd parsing outside of Latvia is not supported")
    print(
        "Type 0 to download all data. THIS WILL DOWNLOAD 8000+ WEBPAGES AND WILL TAKE A LONG TIME!!"
    )

    while True:
        try:
            region = input("")
            if 0 <= int(region) < len(all_regions):
                break
            elif int(region) == len(all_regions):
                print(
                    "Ad parsing outside of Latvia is not supported. Please type the number of the region you are interested in."
                )
            else:
                print(
                    "Invalid input! Please type the number of the region you are interested in."
                )
        except:
            print(
                "Invalid input! Please type the number of the region you are interested in."
            )

    return int(region)


# --------------------------------------------------------
# == END OF USER PROMPTS ==
# --------------------------------------------------------


if __name__ == "__main__":
    main()
