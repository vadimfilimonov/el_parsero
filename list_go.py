#!/usr/bin/python
# -*- coding: utf-8 -*-

# Для того чтобы подключить класс формирования ссылки
import sys
import os
# переходим в корень
sys.path.insert(0, '../')
# Подключаем класс
from links import LinksFormatter

if not os.path.exists('./build'):
	os.mkdir('./build')

# Переменные

# Сайт, с которого происходит парсинг
site = 'clipsite.ru'
# Файл, в котором содержится перечень ссылок, из которых формируется конечный файл с ссылками
file_input = 'list_start.txt'
# Файл, в который помещается результат
file_output = './build/list.txt'
# Класс ссылок, которые нужно помещать файл
linkKeeperClass = "c-blog__button"
# Вызов функции, которая формирует файл
LinksFormatter.goCreateLinks(site, file_input, file_output, linkKeeperClass)

