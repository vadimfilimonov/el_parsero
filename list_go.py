#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

def createBuildFolder():
	if not os.path.exists('./build'):
			os.mkdir('./build')

def goCreateLinks(site, file_input, file_output, linkkeeper):
	input = open(file_input, "r")
	for link in input.readlines():
		html_doc = urlopen(link).read()
		soup = BeautifulSoup(html_doc, "html.parser")
		lists = soup.find_all(class_=linkkeeper)
		links = ''
		for list_item in lists:
			link = 'http://' + site + list_item.find('a').get('href')
			links += link + '\n'
			print(link)
		open(file_output, 'w').close()
		categories_list_result = open(file_output, 'a+')
		categories_list_result.write(links)
		categories_list_result.close()

def start():
	createBuildFolder()
	site = 'clipsite.ru'
	file_input = 'list_start.txt'
	file_output = './build/list.txt'
	linkKeeperClass = "c-blog__button"
	goCreateLinks(site, file_input, file_output, linkKeeperClass)

start()
