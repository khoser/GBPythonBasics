"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
    Подсказка: использовать функцию range() и генератор."""


print('\n'.join(f'{20 + i}' for i in range(221) if not ((20 + i) % 20 and (20 + i) % 21)))
