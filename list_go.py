#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

def createBuildFolder():
	if not os.path.exists('./build'):
			os.mkdir('./build')

def generateLinks(site, file_input, file_output, linkkeeper):
	input = open(file_input, "r")
	for link in input.readlines():
		html_doc = urlopen(link).read()
		soup = BeautifulSoup(html_doc, "html.parser")
		lists = soup.find_all(class_=linkkeeper)
		links = ''
		for list_item in lists:
			link = f'http://{site}{list_item.find("a").get("href")}\n'
			links += link
		open(file_output, 'w').close()
		result = open(file_output, 'a+')
		result.write(links)
		result.close()
		print('Links have been generated!\n')

def start():
	createBuildFolder()
	generateLinks('clipsite.ru', 'list_start.txt', './build/list.txt', 'c-blog__button')

start()
