"""2. Создать текстовый файл (не программно),
    сохранить в нем несколько строк,
    выполнить подсчет количества строк,
    количества слов в каждой строке."""

import os


def word_count(i_string):
    return len(i_string.split(' '))


with open(os.path.join(os.getcwd(), 'task2.txt'), 'r') as file:
    i_text = file.readlines()

print(f'Количество строк: {len(i_text)}')
gen_words = ((i + 1, word_count(i_str)) for i, i_str in enumerate(i_text))
print(f'\n'.join(f'Строка {i} содержит {cnt} слов{"a" if cnt < 5 else ""}' for i, cnt in gen_words))
