# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, num: int):
        self.number_of_cells = num

    def __add__(self, other):
        return f'Сложение клеток: {self.number_of_cells + other.number_of_cells}'

    def __sub__(self, other):
        return f'Вычитание клеток:{abs(self.number_of_cells - other.number_of_cells)}'

    def __mul__(self, other):
        return f'Умножение клеток: {self.number_of_cells * other.number_of_cells}'

    def __truediv__(self, other):
        return f'Деление клеток: {self.number_of_cells // other.number_of_cells}'

    def make_order(self, row_size: int):
        cel = ''
        for i in range(int(self.number_of_cells /row_size)):
            cel += '*' * row_size + '\n'
        cel += '*' * (self.number_of_cells % row_size) + '\n'
        return cel


cell1 = Cell(14)
cell2 = Cell(8)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(7))
