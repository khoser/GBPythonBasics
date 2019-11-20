"""3. Узнайте у пользователя число n.
    Найдите сумму чисел n + nn + nnn.
    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

while True:
    number_n = input('Введите n:\n')
    if number_n.isdigit():
        break
    print('Ожидается число!')

slog1 = int(number_n)
slog2 = int(number_n + number_n)
slog3 = int(number_n + number_n + number_n)

result = slog1 + slog2 + slog3

print(result)