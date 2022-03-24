# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script, work_hours, hourly_rate, bonus = argv


def calс_salary(work_hours_, hourly_rate_, bonus_):
    try:
        result = (int(work_hours_) * float(hourly_rate_)) + float(bonus_)
    except ValueError:
        return
    return result


print("Количество отработанных часов: ", work_hours)
print("Ставка: ", hourly_rate)
print("Бонус: ", bonus)
print(f"Зарплата: {calс_salary(work_hours, hourly_rate, bonus)}")
