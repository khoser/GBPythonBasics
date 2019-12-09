"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
    и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


import os
# import json


def sum_from_string(value: str):
    value_split = (val.split('(') for val in value.split(' '))  # получили генератор списков
    value_splited = (int(val) for val_ar in value_split for val in val_ar if val.isdigit())  # склеили списки в один
    return sum(value_splited)


with open(os.path.join(os.getcwd(), 'task6.txt'), 'r') as file:
    lessons = file.readlines()

lessons_split = (salary.split(':') for salary in lessons)
lessons = {lesson_name: sum_from_string(other_data) for lesson_name, other_data in lessons_split}
# print(json.dumps(lessons))  # попытался через json, но он выводит {"\u0418\u043d\u0444...
print(lessons)
