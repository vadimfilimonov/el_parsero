#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def buildCell(x):
	string_x = str(x)
	no_breakline_x = re.sub("^\\s+|\n|\r|\t|\\s*$|\t*$;", '', string_x)
	single_quote_x = re.sub('"', "'", no_breakline_x)
	wrapped_x = f'"{single_quote_x}"'
	return wrapped_x

def buildRow(*values):
	cells = map(lambda value: buildCell(value), values)
	return ";".join(cells)

def createBuildFolder():
	if not os.path.exists('./build'):
			os.mkdir('./build')

def generateLinks(site, file_input, linkClassname):
	links = []
	parentLinks = open(file_input, "r").read().splitlines()
	for parentLink in parentLinks:
		html_doc = urlopen(parentLink).read()
		soup = BeautifulSoup(html_doc, "html.parser")
		tags = soup.find_all(class_=linkClassname)
		hrefs = map(lambda tag: f'http://{site}{tag.find("a").get("href")}', tags)
		links += hrefs
	return links

def buildCSV(content):
	createBuildFolder()
	open('./build/result.csv', 'w').close()
	result = open("./build/result.csv", "a")
	result.write(content)
	result.close()

def parse(linksList):
	rows = []
	rows.append(buildRow('Title', 'Text', 'Image'))
	for line in linksList:
		html_doc = urlopen(line).read()
		soup = BeautifulSoup(html_doc, "html.parser")
		title = soup.find('h1').text
		text = soup.find('div', 'field--name-body')
		image = soup.find('div', 'c-bg-block').get('style')
		rows.append(buildRow(title, text, image))
		print(title)
	print('All pages have been parsed!')
	content = '\n'.join(rows)
	return content

def start():
	links = generateLinks('clipsite.ru', 'list_start.txt', 'c-blog__button')
	content = parse(links)
	buildCSV(content)

start()
