"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы).
    Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce


def gen_even():
    for elem in range(1001 - 100):
        if not (elem + 100) % 2:
            yield elem + 100


result = reduce((lambda x, y: x * y), (argv for argv in gen_even()))
print(result)

test_res = 1
for elem in range(1001 - 100):
    if not (elem + 100) % 2:
        test_res *= (elem + 100)
print(test_res)

print(result == test_res)