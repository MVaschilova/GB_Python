# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.
salaries_list = []
salaries_all = 0.0
try:
    with open('t3.txt', 'r', encoding='utf-8') as my_file:
        lines = my_file.readlines()
        for line in lines:
            elements = line.split(' ')
            salaries_list.append([elements[0], float(elements[1])])
            salaries_all += float(elements[1])
        print("\nСотрудники с окладом менее 20000 руб.:")
        [print(employee[0]) for employee in salaries_list if employee[1] < 20000]
        print(f'Средняя величина дохода сотрудников составляет {(salaries_all / len(salaries_list)):.2f}')
except IOError:
    print("Ошибка")
