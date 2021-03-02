# coding=utf-8
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
class LinksFormatter:

	@staticmethod
	def goCreateLinks(site, file_input, file_output, linkkeeper):
		# Создаем / Обнуляем счетчик
		counter = 0
		# Открываем входной файл
		input = open(file_input, "r")
		for link in input.readlines():
			html_doc = urlopen(link).read()
			soup = BeautifulSoup(html_doc, "html.parser")

			# Формируем список на основе класса
			lists = soup.find_all(class_=linkkeeper)
			# Пустая переменная для всех ссылок
			links = ''
			# Проходимся по всем элементам
			for list_item in lists:
				# Увеличиваем счетчик на 1
				counter += 1
				# Находим ссылку и извлекаем href
				link = 'http://' + site + list_item.find('a').get('href')
				# Выводим ее в консоль
				print(link)
				# Добавляем в общий список
				links += link + '\n'
			print(counter)
			# Открываем файл
			open(file_output, 'w').close()
			categories_list_result = open(file_output, 'a+')
			# Записываем в файл
			categories_list_result.write(links)
			# И закрываем его
			categories_list_result.close()
