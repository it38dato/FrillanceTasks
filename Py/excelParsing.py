'''Работа с таблицей в excel.
# Разработка Парсинг данных из файла Excel.'''
import openpyxl 
wb = openpyxl.load_workbook('TableIntegratedSites.xlsx')
sheet = wb['Sheet1']
cell = sheet['A2']
print(cell.value)
# или
value = sheet.cell(row=2, column=1).value
print(value)
Source:
# https://sky.pro/media/kak-ispolzovat-python-dlya-raboty-s-excel/ - Чтение данных из файла Excel.