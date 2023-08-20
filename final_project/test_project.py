from project import pricesplit, add_root, extract_cats
from project import strip_values, listify_dict
from project import get_savename, is_listing_page, get_all_links
from project import read_html


def test_spliters():
    assert pricesplit("15 000 €") == (15000, "EUR")
    assert pricesplit("15  €/m2") == (15, "EUR/m2")

    root_url = "https://www.ss.lv"
    assert add_root("/urlextension.html") == "https://www.ss.lv/urlextension.html"
    assert extract_cats("3-1") == (2, 1)


def test_convertors():
    dict1 = {"key1": "/urlextension1.html", "key2": "/urlextension2.html"}
    root_url = "https://www.ss.lv"
    assert strip_values(dict1) == {
        "https://www.ss.lv/urlextension1.html",
        "https://www.ss.lv/urlextension2.html",
    }
    assert listify_dict(dict1) == [
        ("key1", "/urlextension1.html"),
        ("key2", "/urlextension2.html"),
    ]


def test_helpers():
    assert (
        get_savename("https://somedomain.com/this/is/the/filename.html")
        == "the.filename.html"
    )
    assert (
        get_savename("https://somedomain.com/this/is/the/filename")
        == "the.filename.html"
    )

    ppage = read_html("test_ad.html")
    assert get_all_links(ppage, "h2.headtitle") == {
        "Dzīvokļi": "/lv/real-estate/flats/",
        "Bauska un raj.": "/lv/real-estate/flats/bauska-and-reg/",
        "Gailīšu pag.": "/lv/real-estate/flats/bauska-and-reg/gailisu-pag/",
    }
    assert is_listing_page(ppage) == True
