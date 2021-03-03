#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from main import createBuildFolder

def generateLinks(site, file_input, file_output, linkkeeper):
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

def start():
	createBuildFolder()
	generateLinks('clipsite.ru', 'list_start.txt', './build/list.txt', 'c-blog__button')

if __name__ == '__main__':
	start()
