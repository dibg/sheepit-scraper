from bs4 import BeautifulSoup as bs
from json2html import *
from functions.storage import store_as_json, retrieve_json


def generate_html(data):
    html = json2html.convert(data)
    soup = bs(html, "lxml")
    pretty_html = soup.prettify()

    fp = open("index.html", "w")
    fp.write(pretty_html)
    fp.close()


data = retrieve_json("data")
generate_html(data)
