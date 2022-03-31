# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

with open('user_data.txt', 'w+') as my_file:
    user_line = input('Введите строку: ')
    while user_line:
        my_file.write(f"{user_line}\n")
        user_line = input('Введите строку: ')
        if not user_line:
            break
    my_file.seek(0)
    print(my_file.read())
