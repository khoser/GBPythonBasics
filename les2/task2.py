"""2. Для списка реализовать обмен значений соседних элементов,
    т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
    При нечетном количестве элементов последний сохранить на своем месте.
    Для заполнения списка элементов необходимо использовать функцию input()."""

spisok = list()
while True:
    num_of_elems = input('Сколько будет элементов?\n')
    try:
        num_of_elems = int(num_of_elems)
        break
    except ValueError as e:
        print('Ожидается число!')

i = 0
while i < num_of_elems:
    spisok.append(input(f'Введите значение {i}-го элемента списка\n'))
    i += 1

print('Введенный список:\n', spisok)

i = 1
while i < num_of_elems:
    spisok[i-1], spisok[i] = spisok[i], spisok[i-1]
    i += 2

print('После обработки имеем:\n', spisok)
