# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    with open('t2.txt', 'r') as my_file:
        lines = my_file.readlines()
        print(f"Всего строк: {len(lines)}")
        for i, value in enumerate(lines):
            words = value.split(' ')
            print(f"В строке {i + 1} {len(words)} слов")
except IOError:
    print("Ошибка")
