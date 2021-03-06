"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор.
    Функция должна вызываться следующим образом: for el in fibo_gen().
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""


def fibo_gen():
    val = 0
    result = 1
    while val < 15:
        result *= val if val > 0 else 1  # по определению 0! = 1, и я начну вывод с нулевого элемента.
        yield result
        val += 1


for el in fibo_gen():
    print(el)
