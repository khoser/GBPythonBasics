"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

import sys
from itertools import count, cycle

a_b = sys.argv[1]

if a_b == 'a':
    while True:
        num = input('С какого числа начать?\n')
        try:
            num = int(num)
            break
        except ValueError as e:
            print('Ожидается число!')

    while True:
        cnt = input('Сколько элементов вывести?\n')
        try:
            cnt = int(cnt)
            break
        except ValueError as e:
            print('Ожидается число!')

    i = 0
    for el in count(num, 1):
        if i > cnt:
            i = 0
            inext = input('Продолжить? (Y/n)')
            if inext.lower() == 'n':
                break
        print(el)
        i += 1

elif a_b == 'b':
    ar = input('Введите ожидаемый массив, разделяя элементы пробелом\n')
    ar = ar.split(' ')
    while True:
        cnt = input('Сколько раз вывести?\n')
        try:
            cnt = int(cnt)
            break
        except ValueError as e:
            print('Ожидается число!')

    i = 1
    for el in cycle(ar):
        if i > cnt:
            i = 1
            inext = input('Продолжить? (Y/n)')
            if inext.lower() == 'n':
                break
        print(el)
        i += 1
else:
    print('Usage: task6.py <a/b>')
