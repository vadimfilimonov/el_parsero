#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

# Для того чтобы подключить класс формирования ссылки
import sys
# переходим в корень
sys.path.insert(0, '../')

# Подключаем класс
from core.csv import CsvConverter
from core.cleaner import Clear
from core.counter import Count

# Переменные
site = 'https://clipsite.ru'
# Переменная, куда будут попадать значения csv
str_csv = ""

# Файлы
# Файл, в котором хранятся ссылки на страницы с категориями
list_file = open('./list.txt', 'a+')
# Список товаров
result = open("./result.csv", "a+")
# Количество строк в файле со ссылками
filelength = Count.rowsnumber('list.txt')
# Обнуляем счетчик
counter = 0;
# Проходимся по всем ссылкам
for line in list_file.readlines():
	# Библиотека beautiful soup конвертит ссылки в нужный нам формат
	html_doc = urlopen(line).read()
	soup = BeautifulSoup(html_doc, "html.parser")

	# Заголовок страницы
	title = soup.find('h1').text
	title = Clear.delrubbish(title)
	title = CsvConverter.goCSVcell(title)

	# Текст
	text = soup.find('div', 'node__content').find('div', 'field--name-body')
	text = CsvConverter.goCSVcell(text)

	# Изображение
	image = soup.find('div', 'c-bg-block').get('style')
	image = Clear.delrubbish(image)
	image = CsvConverter.goCSVcell(image)

	# Поднимаем счетчик на 1
	counter += 1
	# Выводим в консоль
	print Clear.toBlue(str(counter) + '/' + str(filelength) + ': ') + title
	# Добавляем столбцы в csv
	str_csv += CsvConverter.goCSVrow(str(counter), title, text, image)

# Первая строка таблицы - заголовки столбцов
str_csv_header = CsvConverter.goCSVrow('id', 'Заголовок', 'Текст', 'Изображение')
result.write(str_csv_header)
# Записываем конечный csv файл с категориями
result.write(str_csv)
list_file.close()
result.close()
