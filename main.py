#!/usr/bin/env python

import os
import re
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

def build_cell(value):
    stringed_value = str(value)
    no_breakline_value = re.sub("^\\s+|\n|\r|\t|\\s*$|\t*$;", '', stringed_value)
    single_quote_value = re.sub('"', "'", no_breakline_value)
    wrapped_value = f'"{single_quote_value}"'
    return wrapped_value

def build_row(*values):
    cells = map(build_cell, values)
    return ";".join(cells)

def create_build_folder():
    if not os.path.exists('./build'):
        os.mkdir('./build')

def generate_links(site, file_input, link_classname):
    links = []
    parent_links = open(file_input, "r").read().splitlines()
    for parent_link in parent_links:
        html_doc = urlopen(parent_link).read()
        soup = BeautifulSoup(html_doc, "html.parser")
        tags = soup.find_all(class_=link_classname)
        hrefs = map(lambda tag: f'http://{site}{tag.find("a").get("href")}', tags)
        links += hrefs
    return links

def build_csv(content):
    create_build_folder()
    open('./build/result.csv', 'w').close()
    result = open("./build/result.csv", "a")
    result.write(content)
    result.close()

def parse(links_list):
    rows = []
    rows.append(build_row('Title', 'Text', 'Image'))
    for line in links_list:
        html_doc = urlopen(line).read()
        soup = BeautifulSoup(html_doc, "html.parser")
        title = soup.find('h1').text
        text = soup.find('div', 'field--name-body')
        image = soup.find('div', 'c-bg-block').get('style')
        rows.append(build_row(title, text, image))
        print(title)
    print('All pages have been parsed!')
    content = '\n'.join(rows)
    return content

def start():
    links = generate_links('clipsite.ru', 'list_start.txt', 'c-blog__button')
    content = parse(links)
    build_csv(content)

start()
