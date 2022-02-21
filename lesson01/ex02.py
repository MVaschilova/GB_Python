# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# вариант 1
time_in_sec = int(input("Введите время в секундах >>> "))
hours = time_in_sec // 3600
minutes = time_in_sec // 60 - hours * 60
seconds = time_in_sec % 60
print(time_in_sec, 'секунд - это: {0} часов, {1} минут {2} секунд'.format(hours, minutes, seconds))
print(f'В формате чч:мм:сс {hours:02d}:{minutes:02d}:{seconds:02d}')



