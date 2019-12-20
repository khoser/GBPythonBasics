"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
    уникальные для каждого типа оргтехники."""


class Depot:

    def __init__(self, address, high, area):
        self.address = address
        self.max_high = high
        self.area = area


class Equipment:

    def __init__(self, model, power, paper_formats):
        self.model = model
        self.power = power
        self.paper_formats = paper_formats

    def __str__(self):
        return f'Model: {self.model}, power: {self.power}, available formats: {self.paper_formats}'


class Balance:
    __instance = None
    balance = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, Balance):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, depot = None):
        if not (depot in self.balance.keys()) and depot is not None:
            self.balance[depot] = []

    def __getattr__(self, item):
        return getattr(self.balance, item)


class Printer(Equipment):

    def __init__(self, model, power, paper_formats, colors, velocity):
        super().__init__(model, power, paper_formats)
        self.colors = colors
        self.velocity = velocity


class Scanner(Equipment):

    def __init__(self, model, power, paper_formats, quality):
        super().__init__(model, power, paper_formats)
        self.quality = quality


class Copier(Equipment):

    def __init__(self, model, power, paper_formats, colors):
        super().__init__(model, power, paper_formats)
        self.colors = colors


if __name__ == '__main__':
    p = Printer('canon', 1200, ['a4', 'a5'], 'rgb', 20)
    c = Copier('xerox', 200, ['a4', ], 'rgb')

    d1 = Depot('Север', 6, 200)
    d2 = Depot('Юг', 20, 2000)
    b = Balance()
    bb = Balance(d1)
    print(1)
