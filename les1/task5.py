"""5. Запросите у пользователя значения выручки
    и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма
    (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
    Выведите соответствующее сообщение.
    Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

while True:
    earnings = input('Какова выручка?\n')
    if earnings.isdigit():
        break
    elif earnings.count('.') == 1:
        if earnings.split('.')[0].isdigit() and earnings.split('.')[1].isdigit():
            break
    print('Ожидается числовое выражение!')

while True:
    costs = input('Каковы издержки?\n')
    if costs.isdigit():
        break
    elif costs.count('.') == 1:
        if costs.split('.')[0].isdigit() and costs.split('.')[1].isdigit():
            break
    print('Ожидается числовое выражение!')

earnings = float(earnings)
costs = float(costs)

fin_rez = 'Сработали в ноль'
if earnings > costs:
    print(f'Прибыль {earnings - costs}')
    while True:
        number_of_employees = input('Укажите количество сотрудников:\n')
        if number_of_employees.isdigit():
            number_of_employees = int(number_of_employees)
            break
        print('Ожидается числовое выражение!')
    profit = (earnings - costs) * 100 / earnings
    fin_rez = f'Рентабельность выручки {profit}%\nчто составляет {earnings / number_of_employees} на сотрудника.'
elif earnings < costs:
    fin_rez = f'Убыток {costs - earnings}'

print(fin_rez)
