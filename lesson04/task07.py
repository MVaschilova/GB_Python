# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial


def fact(n):
    for i in range(n):
        yield factorial(i)


try:
    user_num = int(input('Введите число, до которого вычисляем факториал: >> '))
    print('Первые 5 значений: ')
    gen = fact(user_num)
    i = 0
    for elem in gen:
        if (i <= 5 and user_num > 5) or (i < user_num <= 5):
            print(f'{i}! = {elem}')
            i += 1
        else:
            break
except ValueError:
    print('Вы ввели некорректное значение')
