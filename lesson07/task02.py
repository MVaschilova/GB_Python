# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
# ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class WorkingForm(ABC):
    @abstractmethod
    def fabric_calculation(self):
        pass


class Coat(WorkingForm):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_calculation(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suite(WorkingForm):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_calculation(self):
        return round(2 * self.h + 0.3, 2)


class TotalFabric(WorkingForm):
    def __init__(self, v, h):
        self.V = v
        self.H = h

    @property
    def fabric_calculation(self):
        return round((self.V / 6.5 + 0.5) + (2 * self.H + 0.3), 2)


coat = Coat(52)
suite = Suite(1.92)
total = TotalFabric(52, 1.92)
print(f'Расход ткани на костюм: {suite.fabric_calculation} м')
print(f'Расход ткани на пальто: {coat.fabric_calculation} м')
print(f'Общий расход ткани: {total.fabric_calculation} м')
