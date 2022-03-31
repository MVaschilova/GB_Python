# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# # Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

profit = {}
avg_profit = {}
sum_profit = 0
average_profit = 0
i = 0
try:
    with open('t7.txt', 'r', encoding='UTF-8') as my_file:
        my_file.seek(0)
        lines = my_file.readlines()
        for i, line in enumerate(lines):
            company_name, ownership, revenue, costs = line.split()
            profit[company_name] = round(float(revenue) - float(costs), 2)
            sum_profit += profit.setdefault(company_name)
        average_profit = sum_profit / len(lines)
        print(f'Прибыль по компаниям: {profit}')
        avg_profit = {'average_profit': round(average_profit, 2)}
        profit.update(avg_profit)
        print(f'Средняя прибыль: {average_profit:.2f}')
except FileNotFoundError:
    print('Файл не найден')
try:
    with open('t7.json', 'w', encoding='UTF-8') as json_file:
        json.dump(profit, json_file, ensure_ascii=False)
        json_fill = json.dumps(profit, ensure_ascii=False)
        print(f'Содержимое json-файла:\n'
              f'{json_fill}')
except IOError:
    print('Ошибка записи в файл')
my_file.close()
