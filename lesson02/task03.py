# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_num = int(input('Введите порядковый номер месяца: '))

seasons_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
if 12 < month_num < 1:
    print('Номер месяца должен быть числом от 1 до 12')
else:
    print(f'list >> Время года: {seasons_list[month_num - 1]}')

seasons_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
season = seasons_dict.get(month_num)
if season == None:
    print('Номер месяца должен быть числом от 1 до 12')
else:
    print(f'dict >> Время года: {season}')