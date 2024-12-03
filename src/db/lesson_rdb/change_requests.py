import re

file_path = '/Learn_python/src/db/lesson_rdb/Requests2.sql'

with open(file_path, 'r', encoding='UTF-8') as file:
    lines = file.readlines()

pattern = re.compile(r'^\d{2}:\d{2}:\d{2}$')

processed_lines = [line if not pattern.match(line.strip()) else '\n' for line in lines]

with open(file_path, 'w', encoding='UTF-8') as file:
    file.writelines(processed_lines)