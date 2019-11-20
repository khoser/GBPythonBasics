"""4. Пользователь вводит целое положительное число.
    Найдите самую большую цифру в числе.
    Для решения используйте цикл while и арифметические операции."""

while True:
    whole_positive = input('Пользователь, введите целое положительное число:')
    if whole_positive.isdigit():
        break
    print('Ожидается число!')

the_biggest_digit = whole_positive[0]
i = 1
while i < len(whole_positive):
    local_digit = whole_positive[i]
    if int(the_biggest_digit) < int(local_digit):
        the_biggest_digit = local_digit
    i += 1
print('Самая большая цифра - ', the_biggest_digit)
