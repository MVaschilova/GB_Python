# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    def __init__(self, name:str, speed: int, color: str, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево'

    def show_speed(self):
        return f'Скорость автомобиля {self.name}:{self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} превысил скорость. Скорость {self.speed} км/ч'
        else:
            return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'


class SportCar(Car):
    def sport_car(self):
        return f'Спортивная машина {self.name} движется со скоростью {self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} превысил скорость. Скорость {self.speed} км/ч'
        else:
            return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'


class PoliceCar(Car):
    def is_police(self):
        if self.is_police is True:
            return f'Автомобиль {self.name} - полицейская машина'''


town = TownCar('Volkswagen Golf', 63, 'Красный',False)
work = WorkCar('КАМАЗ', 30,'Синий', False)
sport = SportCar('Porsche 911', 120, 'Жёлтый', False)
police = PoliceCar('Police Car', 100, 'Белый', True)

print(f'1. Городской автомобиль: {town.name} цвет: {town.color} \n {town.go()} \n {town.show_speed()} \n {town.turn_left()}\n {town.turn_right()}\n {town.stop()}')
print(f'2. Рабочий автомобиль: {work.name} цвет: {work.color} \n {work.go()} \n {work.show_speed()} \n {work.turn_left()}\n {work.turn_right()}\n {work.stop()}')
print(f'3. Спортивный автомобиль: {sport.name} цвет: {sport.color} \n {sport.go()}\n {sport.show_speed()}\n {sport.turn_left()}\n {sport.turn_right()}\n {sport.stop()}')
print(f'4. Полицейский автомобиль: {police.name} цвет: {police.color} \n {police.go()} \n {police.show_speed()} \n {police.turn_left()}\n {police.turn_right()}\n {police.stop()}')