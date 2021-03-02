#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def delrubbish(x):
	x = re.sub("^\s+|\n|\r|\t|\s*$|\t*$;", '', x)
	x = re.sub('"', "'", x)
	return x

def buildCell(x):
	return f'"{delrubbish(str(x))}"'

def buildRow(*cells):
	row = ''
	for cell in cells:
		row += f'{buildCell(cell)};'
	row += '\n'
	return row

def createBuildFolder():
	if not os.path.exists('./build'):
			os.mkdir('./build')

def start():
	str_csv_body = ""

	list_file = open('./build/list.txt', 'r')
	createBuildFolder()
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
	str_csv_header = buildRow('Заголовок', 'Текст', 'Изображение')
	result.write(str_csv_header)
	result.write(str_csv_body)
	list_file.close()
	result.close()

start()
