# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_length = int(input('Введите размер списка: >>>> '))
list_orig = []
list_mix = []
for i in range(1, list_length + 1):
    item = input(f'Введите значение {i}-го элемента списка: >>> ')
    list_orig.append(item)
    if i % 2 == 0:
        list_mix.append(item)
        list_mix.append(list_orig[i - 2])

if len(list_mix) != list_length:
    list_mix.append(list_orig[list_length - 1])
print(list_orig)
print(list_mix)