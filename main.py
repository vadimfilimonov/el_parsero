#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def buildCell(x):
	x = re.sub("^\\s+|\n|\r|\t|\\s*$|\t*$;", '', x)
	x = re.sub('"', "'", x)
	return f'"{x}"'

def buildRow(*values):
	cells = map(lambda value: f'{buildCell(str(value))};', values)
	return ";".join(cells) + ";\n"

def createBuildFolder():
	if not os.path.exists('./build'):
			os.mkdir('./build')

def generateLinks(site, file_input, file_output, linkkeeper):
	print('Start to generate links')
	input = open(file_input, "r")
	for link in input.readlines():
		html_doc = urlopen(link).read()
		soup = BeautifulSoup(html_doc, "html.parser")
		lists = soup.find_all(class_=linkkeeper)
		links = '\n'.join(map(lambda tag: f'http://{site}{tag.find("a").get("href")}', lists))
		open(file_output, 'w').close()
		result = open(file_output, 'a+')
		result.write(links)
		result.close()
	print('Links have been generated!\n')

def parsePages():
	print('Start to parse pages')
	str_csv_body = ""
	list_file = open('./build/list.txt', 'r')
	open('./build/result.csv', 'w').close()
	result = open("./build/result.csv", "a")
	for line in list_file.readlines():
		html_doc = urlopen(line).read()
		soup = BeautifulSoup(html_doc, "html.parser")
		title = soup.find('h1').text
		text = soup.find('div', 'field--name-body')
		image = soup.find('div', 'c-bg-block').get('style')
		str_csv_body += buildRow(title, text, image)
		print(title)
	str_csv_header = buildRow('Title', 'Text', 'Image')
	result.write(str_csv_header)
	result.write(str_csv_body)
	list_file.close()
	result.close()
	print('All pages have been parsed!')

def start():
	createBuildFolder()
	generateLinks('clipsite.ru', 'list_start.txt', './build/list.txt', 'c-blog__button')
	parsePages()

if __name__ == '__main__':
	start()
