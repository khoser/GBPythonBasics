"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
    У пользователя необходимо запрашивать новый элемент рейтинга.
    Если в рейтинге существуют элементы с одинаковыми значениями,
    то новый элемент с тем же значением должен разместиться после них."""

my_list = [7, 5, 3, 3, 2]

while True:
    i_value = input('Введите новый элемент рейтинга\n')
    try:
        i_value = int(i_value)
        break
    except ValueError as e:
        print('Ожидается число!')

result_list = []
added = False
for val in my_list:
    if not added and i_value > val:
        result_list.append(i_value)
        added = True
    result_list.append(val)
if not added:
    result_list.append(i_value)

print(result_list)
