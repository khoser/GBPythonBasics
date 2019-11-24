"""6. *Реализовать структуру данных «Товары».
    Она должна представлять собой список кортежей.
    Каждый кортеж хранит информацию об отдельном товаре.
    В кортеже должно быть два элемента — номер товара и словарь с параметрами
    (характеристиками товара: название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
    Необходимо собрать аналитику о товарах.
    Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
    а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

characteristics = {'название': str, 'цена': float, 'количество': int, 'единица измерения': str}

tovars = []
i = 0
while True:
    i += 1
    tovar = {}
    for characteristic, its_type in characteristics.items():
        while True:
            try:
                tovar[characteristic] = its_type(input(f'{characteristic}: '))
                break
            except ValueError as e:
                print('Ожидается значение другого типа')
    tovars.append((i, tovar))

    retry = input('\nДобавим следующий товар?\n(y/N):')
    if not retry.upper() == 'Y':
        break

print(tovars)

analytics = {}
for characteristic in characteristics:
    analytics[characteristic] = []

for tovar in tovars:
    for characteristic in characteristics:
        try:
            analytics[characteristic].index(tovar[1][characteristic])
        except ValueError as e:
            analytics[characteristic].append(tovar[1][characteristic])

print(analytics)
