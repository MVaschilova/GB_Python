# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число >>> "))
if number <= 0:
    print('Вы указали не положительное число')
else:
    max_digit = number % 10
number_w = number // 10
while number_w > 0:
    if number_w % 10 > max_digit:
        max_digit = number_w % 10
    number_w = number_w // 10
print(f"Самая большая цифра числа {number} равна {max_digit}")
