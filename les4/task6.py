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
        else:
            print(el)

if a_b == 'b':
    pass
