"""1. Создать список и заполнить его элементами различных типов данных.
    Реализовать скрипт проверки типа данных каждого элемента.
    Использовать функцию type() для проверки типа.
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

spisok = list()
spisok.append(123)
spisok.append('123')
spisok.append("123")
spisok.append(123.0)
spisok.append(f'123')
spisok.append([123, ])
spisok.append((123, ))
spisok.append({})
spisok.append({1, 2, 3})

i = 0  # добавил нумерацию влоб, чтобы было покрасивее. В следующем задании использовал enumerate.
for elem in spisok:
    print(i, ': ', elem, ' is type of ', type(elem))
    i += 1
