#!/usr/bin/env python

import os
import re
from urllib.parse import urlsplit
from urllib.request import urlopen
from bs4 import BeautifulSoup

LINK_CLASS = os.getenv("LINK_CLASS")
TEXT_CLASS = os.getenv("TEXT_CLASS")
IMAGE_CLASS = os.getenv("IMAGE_CLASS")

def build_cell(value):
    stringed_value = str(value)
    no_breakline_value = re.sub("^\\s+|\n|\r|\t|\\s*$|\t*$;", "", stringed_value)
    single_quote_value = re.sub('"', "'", no_breakline_value)
    wrapped_value = f'"{single_quote_value}"'
    return wrapped_value

def build_row(*values):
    cells = map(build_cell, values)
    return ";".join(cells)

def create_build_folder():
    if not os.path.exists("./build"):
        os.mkdir("./build")

def generate_links():
    links = []
    parent_links = open(".pages", "r").read().splitlines()
    site = urlsplit(parent_links[0]).netloc
    for parent_link in parent_links:
        html_doc = urlopen(parent_link).read()
        soup = BeautifulSoup(html_doc, "html.parser")
        tags = soup.find_all(class_=LINK_CLASS)
        hrefs = map(lambda tag: f'http://{site}{tag.find("a").get("href")}', tags)
        links += hrefs
    return links

def build_csv(content):
    create_build_folder()
    open("./build/result.csv", "w").close()
    result = open("./build/result.csv", "a")
    result.write(content)
    result.close()

def parse(links_list):
    rows = []
    rows.append(build_row("Title", "Text", "Image"))
    for line in links_list:
        html_doc = urlopen(line).read()
        soup = BeautifulSoup(html_doc, "html.parser")
        title = soup.find("h1").text
        text = soup.find(class_=TEXT_CLASS)
        image_tag = soup.find(class_=IMAGE_CLASS)
        if image_tag.has_attr("src"):
            image = image_tag.get("src")
        else:
            image = image_tag.get("style")
        rows.append(build_row(title, text, image))
        print(title)
    content = "\n".join(rows)
    return content

def start():
    links = generate_links()
    content = parse(links)
    build_csv(content)
    print("All pages have been parsed!")

start()
