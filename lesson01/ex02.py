# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# вариант 1
time_in_sec = int(input("Введите время в секундах >>> "))
hours = time_in_sec // 3600
minutes = time_in_sec // 60 - hours * 60
seconds = time_in_sec % 60
print(time_in_sec, 'секунд - это: {0} часов, {1} минут {2} секунд'.format(hours, minutes, seconds))

# вариант 2: более компактный способ
time_in_sec_short = int(input("Введите время в секундах >>> "))
print(time_in_sec_short, 'секунд - это {:.0f} часов {:.0f} минут  {:.0f} секунд'.format(time_in_sec // 3600,
                                                                                        time_in_sec // 60 - hours * 60,
                                                                                        time_in_sec % 60))
