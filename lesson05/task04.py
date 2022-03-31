# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = ''
try:
    with open("t4.txt", "r", encoding='utf-8') as my_file:
        new_file = my_file.read()

    for old, new in num_dict.items():
        new_file = new_file.replace(old, new)
except IOError:
    print("Ошибка")
with open('new_t4.txt', 'w', encoding='utf-8') as replaced_file:
    replaced_file.write(new_file)
    replaced_file.close()
