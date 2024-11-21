# -*- coding: cp1251 -*-
# -*- coding: utf-8 -*-
import matplotlib
import inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pathlib
from pathlib import Path

# import requests
# from requests import get
# import chardet
# import sys
# import codecs
# import fileinput, pathlib

# url = 'http://jira.it-mentor.tech/secure/attachment/15415/15415_lorum.txt'
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     content = response.text
#     print(content)

# with open(r'C:\Users\Admin\Downloads\datasets\lorum.txt', 'r', encoding='utf-8') as file:
#
#     print(file.read())
#     file.seek(0)
#     print(file.readlines())
#     file.seek(0)
#     print(list(file))
#     file.seek(0)
#     line = file.readline()
#     while line != '':
#         print(line, end='')
#         line = file.readline()
#     print()
#     file.seek(0)
#     for _ in file.readlines():
#         print(_, end='')
#     print()
#     file.seek(0)
#     for _ in file:
#         print(_, end='')
#     file.flush()

# text = ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']
#
# with open(r'C:\Users\Admin\Downloads\foo1.txt', 'w', encoding='utf-8') as file:
#     file.write('Создаём файл с данными\n')
#     for line in text:
#         file.write(line + '\n')
#     print(file.tell())

# read_file = r'C:\Users\Admin\Downloads\foo.txt'
# write_file = r'C:\Users\Admin\Downloads\new_foo.txt'

# text = ['Строка №6', 'Строка №7', 'Строка №8', 'Строка №9', 'Строка №10']
#
# with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w', encoding='utf-8') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)
#
# with open(r'C:\Users\Admin\Downloads\foo.txt', 'a', encoding='utf-8') as file:
#     file.write('\n\n')
#     file.write('Добавляем данные в файл\n')
#     for line in text:
#         file.write(line + '\n')
#
# with open(r'C:\Users\Admin\Downloads\foo.txt', 'r', encoding='utf-8') as file:
#     print(file.read())
#     print(file.tell())
#     file.seek(274)
#     print(file.read(1))

# print()
# print(fr.closed)
# print(type(fw))


# if sys.platform.startswith('win'):
#     import os
#     os.system('chcp 65001')
#
# codecs_list = ["cp437", "utf-16be", "utf-16", "cp1252", "ascii", "utf-8", "windows-1251", "ISO-8859-1"]
# for codec in codecs_list:
#     try:
#         with open(r'C:\Users\Admin\Downloads\lorum.txt', "r", encoding=codec) as file:
#             text = file.read()
#         print(codec, "|", text)
#     except (UnicodeDecodeError, FileNotFoundError, OSError) as e:
#         print(codec, "|", "Ошибка:", e)

# with open(r'C:\Users\Admin\Downloads\lorum.txt', 'rb') as file:
#     rawdata = file.read(10000)  # Читаем первые 10000 байт
#     result = chardet.detect(rawdata)
#     encoding = result['encoding']
#     print(f'Определенная кодировка: {encoding}')
#
#     # Чтение файла с определенной кодировкой
#     with open(r'C:\Users\Admin\Downloads\lorum.txt', 'r', encoding=encoding) as file:
#         text = file.read()
#     print(text)

# pth = r'C:\Users\Admin\Downloads\texts'
# pattern = '*.txt'
#
# files_path = pathlib.Path(pth)
# files_list = files_path.glob(pattern)
# file_new = 'file_new.all'
#
# if files_list:
#     with fileinput.FileInput(files=files_list) as fr, open(file_new, 'w') as fw:
#         for line in fr:
#             if fr.isfirstline():
#                 file_name = fr.filename()
#                 fw.write(f'\n\n-----------{file_name}\n\n')
#             fw.write(line)

# r'C:\Users\Admin\Downloads\bikes.csv'

# pd.set_option('display.max_columns', None)
#
# work_path = pathlib.Path(r'C:\Users\Admin\Downloads')
# data_path = work_path / 'datasets' / 'bikes.csv'
# print(data_path)
# data = pd.read_csv(data_path)
# print(data.head(8))
# sum_value = data['Rachel1'].sum()
# print(sum_value)

# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 5)
#
# bikes = pd.read_csv(r'C:\Users\Admin\Downloads\datasets\bikes.csv', sep=',', encoding='latin1',
#                        parse_dates=['Date'], dayfirst=True, index_col='Date')
# print(bikes[:3])
# bikes['Berri 1'].plot()
# #fixed_df.plot(figsize=(15, 10))
# berri_bikes = bikes[['Berri 1']].copy()
# print(berri_bikes[:5])
# print(berri_bikes.index.weekday)
# berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
# print(berri_bikes[:5])
# weekday_counts = berri_bikes.groupby('weekday').aggregate('sum')
# print(weekday_counts)
# weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(weekday_counts)
# weekday_counts.plot(kind='bar')
# plt.show()

# pd.options.display.max_rows = 7
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 3)
# #plt.rcParams['font.Family'] = 'sans-serif'
# # complaints = pd.read_csv(r'C:\Users\Admin\Downloads\datasets\311-service-requests.csv')
# # complaint_counts = complaints['Complaint Type'].value_counts()
# # complaint_counts[:10].plot(kind='bar')
# requests = pd.read_csv(r'C:\Users\Admin\Downloads\datasets\311-service-requests.csv')
# print(requests['Incident Zip'].unique())
# na_values = ['NO CLUE', 'N/A', '0']
# requests = pd.read_csv(r'C:\Users\Admin\Downloads\datasets\311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})
# print(requests['Incident Zip'].unique())
# rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
# print(len(requests[rows_with_dashes]))
# print(requests[rows_with_dashes]['Incident Zip'])
# long_zip_codes = requests['Incident Zip'].str.len() > 5
# print(requests['Incident Zip'][long_zip_codes].unique())
# requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
# print(requests[requests['Incident Zip'] == '00000'])
# zero_zips = requests['Incident Zip'] == '00000'
# requests.loc[zero_zips, 'Incident Zip'] = np.nan
# unique_zips = requests['Incident Zip'].unique()
# print(unique_zips)
# zips = requests['Incident Zip']
# is_close = zips.str.startswith('0') | zips.str.startswith('1')
# is_far = ~(is_close) & zips.notnull()
# print(zips[is_far])
# print(requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip'))
# print(requests['City'].str.upper().value_counts())

#plt.show()

# pd.options.display.max_rows = 7
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 3)
# plt.rcParams['font.family'] = 'sans-serif'
# #weather_2012_final = pd.read_csv(r'C:\Users\Admin\Downloads\datasets\weather_2012.csv', index_col='Date/Time')
# #weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
# url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
# url = url_template.format(month=3, year=2012)
# weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1')
# print(weather_mar2012)

# plt.style.use('ggplot')  # Красивые графики
# plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок
# popcon = pd.read_csv(r'C:\Users\Admin\Downloads\datasets\popularity-contest.txt', sep=' ')[:-1]
# popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
# print(popcon[:5])
# popcon['atime'] = popcon['atime'].astype(int)
# popcon['ctime'] = popcon['ctime'].astype(int)
# popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
# popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')
# print(popcon['atime'].dtype)
# print(popcon[:5])
# popcon = popcon[popcon['atime'] > '1970-01-01']
# nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
# print(nonlibraries.sort_values('ctime', ascending=False)[:10])