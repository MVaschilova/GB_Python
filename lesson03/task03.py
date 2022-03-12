# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.
def sum_2_of_3(a, b, c):
    try:
        fn_list = [a, b, c]
        fn_list.sort(reverse=True)
        result = fn_list[0] + fn_list[1]
    except ValueError:
        return
    return result


try:
    a_1 = float(input("a:  >>> "))
    b_1 = float(input("b: >>> "))
    c_1 = float(input("c: >>> "))
    print(f"Сумма двух наибольших элементов = {sum_2_of_3(a_1, b_1, c_1)}")
except ValueError:
    print('Вы ввели некорректные значения')
