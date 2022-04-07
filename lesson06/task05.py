# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} на бумаге')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} на кульмане')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} на школьной доске')


pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашем')
pencil.draw()
handle = Handle('маркером')
handle.draw()
something = Stationery('угольком')
something.draw()