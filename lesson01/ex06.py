# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

start_km = float(input('Укажите первоначальную длину пробежки в км: >> '))
finish_km = float(input('Укажите целевое значение длины пробежки в км: >> '))
if finish_km < start_km or finish_km < 0 or start_km < 0:
    print('Вы указали некорректные входные данные')
else:
    days_num = 0
while start_km < finish_km:
    days_num += 1
    start_km += 0.1 * start_km
print(days_num)
# или полное сообщение:
print(f'На {days_num}-й день спортсмен будет пробегать не менее {finish_km} километров')