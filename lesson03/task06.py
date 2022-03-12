#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#  но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
from typing import List, Any
from unittest import result

alphabet = set('abcdefghjklmnopqrstuvwxyz')


def match(word):
    return bool(set(word).issubset(alphabet))


def int_func(word):
    if match(word):
        return word.title()


# альтернативный вариант функции

def int_func_alt(word):
    if match(word):
        return word[:1].upper() + word[1:]


my_string_1 = []
my_string_2 = []
try:
    for i in input('Введите строку латиницей в нижнем регистре, слова в которой разделены пробелами: ').split(' '):
        my_string_1.append(int_func(i))
        my_string_2.append(int_func_alt(i))
    print(f'{" ".join(my_string_1)}')
    print(f'{" ".join(my_string_2)}')
except Exception:
    print('Вы ввели некорректные значения')
