"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import sys

USAGE = f'Usage: task1.py <hours: float> <rate: float> [<bonus: float>]'


def calc_value(hours, rate, bonus):
    return rate * hours + bonus


let_exit = False
params = sys.argv
if len(params) < 3:
    let_exit = True

bonus = 0
try:
    if len(params) >= 3:
        hours, rate = float(params[1]), float(params[2])
    if len(params) > 3:
        bonus = float(params[3])
except ValueError as e:
    let_exit = True

if let_exit:
    print(USAGE)
else:
    result = calc_value(hours, rate, bonus)
    print(f'Расчет показывает {result}руб.')
