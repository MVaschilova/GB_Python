# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран

from random import randint

my_list = [randint(-100, 100) for i in range(10)]
space = ''
with open('t5.txt', 'w+') as my_file:
    for i in my_list:
        my_file.write(space + str(i))
        space = ' '
    my_file.seek(0)

    nums_str = my_file.read()
    nums = nums_str.split(' ')
    print('Набор чисел в файле:')
    print(nums_str)
    print(f'Сумма чисел файла = {sum([int(i) for i in nums])}')
my_file.close()
