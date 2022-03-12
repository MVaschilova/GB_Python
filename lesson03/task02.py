# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_user(name, surname, birth_year, city, email, phone):

    print(f"Пользователь {name} {surname}, {birth_year} года рождения, город проживания {city}, Email: {email}, "
          f"телефон: {phone}")


user_tmp = {
    'name': 'Введите имя пользователя',
    'surname': 'Введите фамилию',
    'birth_year': 'Укажите год рождения',
    'city': 'Укажите город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
user_data = {}
for key, value in user_tmp.items():
    input_value = input(f'{value}: ')
    user_data.update({key: input_value})

print_user(**user_data)
