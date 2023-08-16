# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_square(self):
        return round(pi * self.radius ** 2, 2)

    def get_circle(self):
        return round(2 * pi * self.radius, 2)


circle = Circle(int(input('Введите радиус: ')))
# или так:
# radius = int(input('Введите радиус: '))
# circle = Circle(radius)
print(f'Площадь: {circle.get_square()}\nДлина окружности: {circle.get_circle()}')
