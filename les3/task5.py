"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
    При нажатии Enter должна выводиться сумма чисел.
    Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение программы завершается.
    Если специальный символ введен после нескольких чисел,
    то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""


ar_sum = []  # я не придумал как решить через функцию, потому что не увидел как что попереиспользовать
sp_char = input('Каков будет спецсимвол?\n')
print('Теперь ожидаем числа, введенные через пробел')
its_time_to_go = True
while its_time_to_go:
    ar_str = []  # для вывода того, что не отработали из текущего ввода
    str_sum = input()
    str_sum = str_sum.split(' ')
    for item in str_sum:
        try:
            var = float(item)
        except ValueError as e:
            if sp_char in item:  # проверим на спецсимвол
                its_time_to_go = False
                break
            ar_str.append(item)
            continue
        ar_sum.append(var)
    print(f'Не обработаны: {[item for item in ar_str]}')
    print(f'Сумма {sum(ar_sum)}')
    print('Продолжаем' if its_time_to_go else '')
