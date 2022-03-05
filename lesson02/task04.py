# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите несколько слов через пробел: >> ')
user_string = user_string.strip()
words_list = user_string.split(' ')
print(words_list)
counter = 1
for i in words_list:
    print(f'{counter}. {i[0:10]}')
    counter += 1

