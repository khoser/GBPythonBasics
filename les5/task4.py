"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

import os


translation = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    }

with open(os.path.join(os.getcwd(), 'task4.txt'), 'r') as file:
    numbers = file.readlines()

for key, value in translation.items():
    numbers = [nline.replace(key, value) for nline in numbers]

with open(os.path.join(os.getcwd(), 'task4_out.txt'), 'w') as file:
    file.writelines(numbers)
