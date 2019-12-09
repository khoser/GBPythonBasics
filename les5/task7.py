"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
    название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""


import os
import json


def avg_profit(firms_dict):
    firms_ar = [val_ar for val_ar in firms_dict.values() if val_ar >= 0]
    if len(firms_ar) == 0:
        return 0
    return sum(firms_ar)/len(firms_ar)


cwd = os.getcwd()
with open(os.path.join(cwd, 'task7.txt'), 'r', encoding='utf8') as file:
    firms = file.readlines()
firms_data = [firm.split(' ') for firm in firms]
firms_dict = {firm[0]: int(firm[2]) - int(firm[3]) for firm in firms_data}
result = [firms_dict, {'average_profit': avg_profit(firms_dict)}]

json_data = json.dumps(result)

with open(os.path.join(cwd, 'task7_out.txt'), 'w', encoding='utf8') as file:
    file.write(json_data)
