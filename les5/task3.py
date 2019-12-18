"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников."""

import os


with open(os.path.join(os.getcwd(), 'task3.txt'), 'r') as file:
    salary_lines = file.readlines()
salary_split = [salary.split(',') for salary in salary_lines]
salary_float = {surname: float(salary) for surname, salary in salary_split}
print(f'Зарплата меньше 20000:')
print(f'\n'.join(f'{surname}' for surname, salary in salary_float.items() if salary < 20000))

avg_salary = sum(salary_float.values()) / len(salary_float)
print(f'Средняя величина {avg_salary}')
