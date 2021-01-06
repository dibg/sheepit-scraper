from bs4 import BeautifulSoup as bs
from json2html import *


def generate_html(data):
    html = json2html.convert(data)
    soup = bs(html, "html.parser")
    pretty_html = soup.prettify()

    fp = open("index.html", "w")
    fp.write(pretty_html)
    fp.close()
