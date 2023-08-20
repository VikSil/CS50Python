# LATVIAN REAL-ESTATE MARKET WEB SCRAPER

>The most popular advertisement site in Latvia is [www.ss.lv](www.ss.lv). The site's popularity and the small size of Latvia at only 1.8 million population, makes it an ideal candidate for gathering market data that is representative of the country's real-estate market. It is almost entirelly built on HTML (with some JavaSript sprinkled in) allowing for automated data scraping of individual adverts using Python Beautiful Soup library.

## Video demo

>Click on the image below to watch the video demo if you are in the hurry and don't have time to read the description below.

[![WEB SCRAPER VIDEO DEMO](https://i.imgur.com/bGMHhSD.png)](https://youtu.be/OLbTlyNELxY)


## Functionality

>This section goes into more detail of what the script can do and how it does it.

### Limitations

>There are a few limitations to the functionality that you should be aware of:

+ This is a concept project and is not intended as a complete solution. The aim of the project is to demontrate that it is in principal possible to automate data gathering from an advertisement website by parsing HTML using Python. For the purposes of CS50 Python course final functionality for downlading appartment data has been developed. It is not possible to download data on houses, vehicles, items for sale, labour market etc.
+ Only adverts for the flats being sold or leased out will be parsed. Adverts on the supply side usually have well defined structure with clearly stated price and characteristics of the appartment that can be easily extracted from the appropriate HTML tags. People looking to rent or buy an appartment tend to be vague/flexible about what they are looking for and will state a range of price and characteristics as free text. This is less suitable for parsing and is beyond the scope of this project.
+ Only advertisements about appartments in Latvia will be parsed. The site offers a very small set of adverts pertaining to properties outside of Latvia. These have been excluded from the project.
+ This code is not intended for commercial use, but educational purposes only. At the time of writing (August 2023), to the best of author's knowledge, the project is compliant with Latvian and international laws.

---

### What is [ss.lv](www.ss.lv)?

>In this context, "**ss**" stands for "_sludinājumu serviss_", or "_advertisement service_" when translated to English. It is the largest advertisement site in Latvia. The interface of the site is all in Latvian (with optional Russian), but this guide will talk you through the things you need to know. Depending on what browser you use, your browser may also offer auto-translate when visiting the site.

>The landing page of the site looks like this:

<p align="center">
<img src=https://i.imgur.com/ocaerp2.png>
</p>

>All the adverts on the site are divided into several categories with a number of sub-categories. The appartment sub-category (lat: "Dzīvokļi") is the first sub-category nested under Real-Estate (lat: "Nekustamie īpašumi"), highlighted in the image above.

>In turn appartment adverts are divided into regional groups. The number in brackets next to each region signifies the total number of adverts for that region. Latvia's capital city Riga (lat: "Rīga") is split out from it's region (lat: "Rīgas rajons"), since it accounts for more than half of total number of adverts on its own.

<p align="center">
<img src=https://i.imgur.com/ThVyGqL.png>
</p>

>Each region with more than 200 adverts will lead to yet another sub-category page, this time spliting all adverts in the region by parish (or borough - in the case of Riga and Jurmala cities). However, all region pages will include a link leading to a listing with all adverts (lat: "Visi sludinājumi") for that region.

<p align="center">
<img src=https://i.imgur.com/unTtYwE.png>
</p>

>A listing page contains summary data for individual adverts - one advert per line. It displays an image (if suplied by the author of the advert), truncated description, location of the property, number of rooms, living area of the appartment, the type of the house the appartment is located in and on what level, as well as the price of the property. Each listing may have several tabs/pages that can be clicked through at the bottom of the page. Adverts in Latvian and Russian are equaly common on the site, since Latvia has a sizeable Russian minority at about a quarter of the country's population.

<p align="center">
<img src=https://i.imgur.com/fRQp0Oo.png>
</p>

>When an individual line in the listing is clicked, it will open a page with all of the data pertaining to the particular property. At a minimum this will contain full description of the property, price and currency (the currency used in Latvia is Euro), and all of the other details that were previously visible on the listing page. An example advert looks like this:

<p align="center">
<img src=https://i.imgur.com/7RZG68l.png>
</p>

>In adition the street name and house number will also be included. Some properties mention ameneties such as a balcony, metal doors or plastic windows, but these are not taken into account by the data scraper.

---

### How to use the data scraper?

>Run the program from the project directory by typing this command:

python project.py

>The program may take a few seconds to start. Once it starts, it will explain it's purpose, display instructions on how to use it and prompt you to press Enter to proceed.

<p align="center">
<img src=https://i.imgur.com/QitplcF.png>
</p>

>The first page that the program will download is the landing page of the advertisement site. It will diplay all the categories and sub-catgories as an enumerated list. You will then be prompted to input the category and sub-category to download data from.

<p align="center">
<img src=https://i.imgur.com/NhOQErp.png>
</p>

>For the purposes of CS50 Python course final project only appartment data parsing has been implemented. To test the program you must input this category code exactly: **3-1**

<p align="center">
<img src=https://i.imgur.com/jv2bIUU.png>
</p>

>The program will proceed to download and parse the region page of appartment adverts. The list of regions will be output in an enumerated format and you will be prompted for the region number. It is not possible to input multiple regions, but it is possible to download  all data by inputing zero as the region number. <span style="color:red">**Doing so will take a long time and is not recommended, as it puts undue load onto the advertisement server.**</span>

<p align="center">
<img src=https://i.imgur.com/MQwTCVU.png>
</p>

>Following the region number you will be prompted for the file name to output data to. Feel free to input only the file name without the extension. The program will add the Excel extention automatically. Once the file name is supplied, the program will start to work on preparing the data. There may be a pause in output if you chose to download data for a large region or the capital city of Riga. Please be patient.

<p align="center">
<img src=https://i.imgur.com/cHZLAXw.png>
</p>

>Once the program has gathered all the links to individual adverts, it will start parsing through them and output URL to each advert as it goes through the list. Once all adverts for a region are processed, the program will output the data into the output Excel file and display a notification about it.

<p align="center">
<img src=https://i.imgur.com/98ZtUWz.png>
</p>


>To download the output Excel file, right click on the file name and choose "Download..." from the context menu. This will prompt a dialog window allowing you to download the file onto the local harddrive.

<p align="center">
<img src=https://i.imgur.com/kAPETkr.png>
</p>

>The output file will contain data from the parsed adverts.

<p align="center">
<img src=https://i.imgur.com/2miwwax.png>
</p>

---

## Code architecture

>This section goes into more detail of how the code is constructed and how it does what it does.

### Beautiful Soup

>Beautiful Soup is a python library for scraping web data from HTML documents. It is not a part of python distribution and needs to be installed separately. To install Beautiful Soup run the following code in the console:

```
    pip install beautifulsoup4
````

>Documentation on the library can be found [here](https://pypi.org/project/beautifulsoup4/).

>This web-scraper uses Beautiful Soup to access webpages, download them and parse HTML to find specific tags and their content. The content of the tags is then cleaned, transformed and combined into data structures and objects inside the program and ultimatelly - in the output data.

### Class hierarchy

>Two custom classes have been created for this program. Both can be found in the `advertisements.py` file.

+ The higher abstraction class **_`Ad`_** implements the basic atributes common to all adverts: url, advert type, description, price and currency, as well as named atributes of fractional price and fraction unit (i.e. per month or m2).
+ The extended class  **_`Flat`_** has additional atributes of city, area and rooms, as well as named atributes of parish, village, street, building series, type and level at which the flat is situated in the building. All of the named atribues are defaulted to an empty string.

>Both classes have the following methods implemented:

+ **\_\_`init`__** : the default initialisation method
+ **\_\_`str`__** : outputs all atribute values of an object as a human readable text when the object is passed as an argument to `print()` function
+ **`listmyself`** : outputs all atribute values in a list that can be passed onto a function to save as an Excel file

### Main function

>The `main()` function ties together all website requests, Ad object creation, data manipulation and output to Excel into a seamless workflow. The high abstraction of the algorythm is as follows:

1. Retrieve the landing page HTML
2. Parse the landing page into a list of categories and subcategories
3. Display the enumerated categories to the user prompting for a category number
4. Parse and verify user input
5. Retrieve HTML of the category page
6. Parse the category page and list all regions
7. Display the enumerated regions to the user prompting for a region number
8. Verify user input
9. Retrieve HTML of the region page
10. Verify that the region page is a listing page
    +  If not then retrieve the HTML for all adverts from the region page
11. Iterate through the listing and retrieve all URLS to all tabs/pages of listing
12. Iterate through all links to tabs/pages of a listing and retrieve all links to individual adverts
13. Iterate throught all adverts and scrape advert data adding each to a list of lists
14. Convert the list of lists to a dataframe and output to Excel

### Output to Excel

>Python libraries `openpyxl` and `pandas` are required to output data to Excel. These are not part of python distribution and need to be installed separately. To install openpyxl and pandas run the following code in the console:

```
    pip install pandas
    pip install openpyxl
```

>Documentation on the pandas library can be found [here](https://pandas.pydata.org/).

>Documentation on the openpyxl library can be found [here](https://openpyxl.readthedocs.io/en/stable/).

>The advert data gathered by the program is transformed to pandas Dataframe structure. Dataframe class has `ExcelWriter` method to output  the dataframe data to Excel format. It requires an Excel read/write engine, such as openpyxl to save the data.
