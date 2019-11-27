"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой."""


def func(name: str = None,
         surname: str = None,
         birthday: str = None,
         city: str = None,
         email: str = None,
         phone: str = None):
    return (f'Пользователь {name} по фамилии {surname} родился {birthday}, на данный момент проживает в г. {city}.\n' +
            f'Контактные данные: тел. {phone}, e-mail {email}.')


user = {'name': 'Олег',
        'surname': 'Х',
        'birthday': '19.10',
        'city': 'Саратов',
        'email': 'email@mail.ru',
        'phone': '+79876543210'
        }
print(func(**user))
