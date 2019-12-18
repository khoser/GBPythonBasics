"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os
from random import randint

# как и во всех остальных заданиях, сначала готовлю данные, потом пишу в файлы.
numbers = [randint(0, 100) for _ in range(randint(5, 10))]
str_numbers = (str(num) for num in numbers)
with open(os.path.join(os.getcwd(), 'task5.txt'), 'w') as file:
    file.write(' '.join(str_numbers))
sum_numbers = sum(numbers)
print(f'Сумма = {sum_numbers}')
