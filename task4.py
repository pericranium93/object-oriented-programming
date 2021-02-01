import random


def info(car):
    car.get_info()
    car.go()
    car.stop()
    car.turn_direction()
    car.show_speed()


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.__is_police = False

    def go(self):
        print(f'{self.name} поехала вперед')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_direction(self):
        if random.randrange(2):
            print(f'{self.name} повернула направо')
        else:
            print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed} км/ч')

    def get_info(self):
        print({'Название': self.name, 'Цвет': self.color})
        if self.__is_police:
            print(f'Это полицейский автомобиль')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость выше разрешенной на {self.speed - 60} км/ч')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость выше разрешенной на {self.speed - 40} км/ч')


class SportCar(Car):
    def met(self):
        pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._Car__is_police = True



a = Car(random.randrange(101), 'green', 'Vishnyovaya devyatka')
info(a)

b = TownCar(random.randrange(151), 'yellow', 'Hyundui Polaris')
info(b)

c = WorkCar(random.randrange(80), 'grey', 'Namaz')
info(c)

d = SportCar(random.randrange(251), 'white', 'HeRReRa')
info(d)

e = PoliceCar(random.randrange(201), 'special', 'KDV')
info(e)