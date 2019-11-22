"""2. Пользователь вводит время в секундах.
    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
    Используйте форматирование строк."""

while True:
    while True:
        t_qt_sec = input('Сколько секунд обсчитать?\n')
        if t_qt_sec.isdigit():
            break
        print('Ожидается число!')

    qt_sec = int(t_qt_sec)
    qt_hour = qt_sec // 60 // 60
    qt_mnts = (qt_sec % (60 * 60)) // 60
    qt_sec %= 60

    result = f'{qt_hour}:{qt_mnts}:{qt_sec}'

    print('Результат: ', result)

    retry = input('\nПовторим?\n(y/N):')
    if not retry.upper() == 'Y':
        break
