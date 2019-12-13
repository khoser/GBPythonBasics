"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса.
    Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу:
длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
    Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


class Road:
    WEIGHT1M2 = 25  # кг/см - вес одного квадратного метра толщиной в 1 см

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, depth):
        return depth * self.WEIGHT1M2 * self._width * self._length


if __name__ == '__main__':
    road_Saratov_Piter = Road(1500, 20)
    print(road_Saratov_Piter.weight(5))
    print(road_Saratov_Piter._length)
    print(road_Saratov_Piter._width)
