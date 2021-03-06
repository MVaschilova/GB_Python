# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) — Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

subject_dict = {}
try:
    with open('t6.txt', 'r', encoding='UTF-8') as my_file:
        lines = my_file.read()
        my_file.seek(0)
        for line in my_file:
            row_items = line.split(':')
            hours = re.findall(r"\d+", row_items[1])
            subject_dict.update({row_items[0]: sum([int(i) for i in hours])})
    print(f'Содержимое файла \n{lines}'
            f'{subject_dict}')
except FileNotFoundError:
    print('Файл не найден')