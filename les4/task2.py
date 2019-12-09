"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
    значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

# Я понял условие так: нужно пробежаться по списку и если текущий элемент больше предыдущего, то его надо выводить.
# Если же надо пробежаться по списку и выбирать все элементы, которые больше текущего, то будет список списков в конце.

import sys


def gen_numb(ar):
    i0 = min(ar) - 1  # беру минимальный для того, чтобы первый с чем-то сравнить, ибо в задаче про первый не сказано.
    for elem in ar:      # а так как перед первым ничего нет, то будем считать, что он больше этой пустоты.
        if elem > i0:
            yield elem
            i0 = elem


params = sys.argv[1:]
let_exit = False
try:
    for i in enumerate(params):
        params[i[0]] = int(i[1])  # для простоты будем считать целыми числа
except ValueError as e:
    print(f'На входе ребуется список чисел.')
    let_exit = True

if not let_exit:
    print('\n'.join(f'{elem}' for elem in gen_numb(params)))
