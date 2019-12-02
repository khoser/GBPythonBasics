"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию.
    Элементы вывести в порядке их следования в исходном списке.
    Для выполнения задания обязательно использовать генератор."""

import sys


def gen_dist(ar):
    for elem in ar:
        if ar.count(elem) == 1:
            yield elem


params = sys.argv[1:]
let_exit = False
try:
    for e_elem in enumerate(params):
        params[e_elem[0]] = int(e_elem[1])  # для простоты будем считать целыми числа
except ValueError as e:
    print(f'На входе ребуется список чисел.')
    let_exit = True

if not let_exit:
    print('\n'.join(f'{elem}' for elem in gen_dist(params)))
