# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
user_digit = int(input("Введите цифру >>> "))
if user_digit // 10 != 0:
    print('Вы указали некорректное значение')
else:
    print(
        3 * user_digit + 20 * user_digit + 100 * user_digit)  # произведено арифметическое упрощение выражения n + nn + nnn
