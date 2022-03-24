# 6. Реализовать два небольших скрипта:
#     а) итератор, генерирующий целые числа, начиная с указанного,
#     б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, islice
from itertools import cycle

while True:
    try:
        srart_num = int(input('Введите число, с которого начнётся генерация 10 целых чисел: >> '))
        for el in islice(count(srart_num), 10):
            print(el, end=' ')
        break
    except ValueError:
        print('Вы ввели некорректное значение')

print('\n ===========================================================================================')
с = 0
my_list = ['w', 'o', 'r', 'l', 'd']
print(f'Повтор элементов списка {my_list} трижды:')
for el in cycle(my_list):
    if с > len(my_list) * 3 - 1:
        break
    print(el, end=' ')
    с += 1
