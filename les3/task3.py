"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов."""


def my_func(var1: float, var2: float, var3: float) -> float:
    """
    Вернём сумму двух наибольших!
    :param var1: float
    :param var2: float
    :param var3: float
    :return: float
    """
    return var1 + var2 + var3 - min(var1, var2, var3)


print(my_func(-1, 2, 3))
print(my_func(2, 3, -1))
print(my_func(3, 2, -1))
print(my_func(2, -1, 3))
