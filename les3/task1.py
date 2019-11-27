"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def func(var1: float, var2: float, *args, **kwargs) -> float or None:
    """
    Делим первое значение на второе.
    :param var1: float - делимое
    :param var2: float - делитель
    :param args: прочее
    :param kwargs: для совместимости
    :return: float - частное от деления, или None, если делитель 0.
    """
    if var2:
        return var1 / var2
    return None


while True:
    var1 = input('Введите делимое\n')
    try:
        var1 = float(var1)
        break
    except ValueError as e:
        print('Ожидается число!')
while True:
    var2 = input('Введите делитель\n')
    try:
        var2 = float(var2)
        break
    except ValueError as e:
        print('Ожидается число!')

print(func(var1, var2))
