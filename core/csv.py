# coding=utf-8
class CsvConverter:

	# Конверт входного значения в приемлимый для csv вид
	@staticmethod
	def goCSVcell(x):
		# Оборачиваем в в двойные кавычки и задаем кодировку
		x = '"' + x.encode('utf-8') + '"'
		return x

	# Конверт ячеек в строку
	@staticmethod
	def goCSVrow(*cells):
		# Создаем пустую строку
		row = ''
		# Проходимся по всем ячейкам
		for cell in cells:
			# Каждой ячейке справа добавляем точку с запятой
			row += cell + ';'
		# У последнего столбца добавляем перенос строки
		row += '\n'
		return row