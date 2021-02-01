def check(param, unit):
    value = input(f'{param} полотна в {unit}.')
    while True:
        try:
            value = float(value)
            if value <= 0:
                value = input(f'{param} не может быть меньше 1')
            else:
                print(f'{param} = {value} {unit}')
                return value
        except ValueError:
            value = input(f'{param} полотна в {unit}.')


class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness
        self.__mass_per_m = 25

    def mass(self):
        return self._length * self._width * self.__mass_per_m * self._thickness / 1000


length = check('Длина', 'м')
width = check('Ширина', 'м')
thickness = check('Толщина', 'см')
new_road = Road(length, width, thickness)
print(f'Для создания дороги потребуется {new_road.mass(): .2f} т. асфальта')
