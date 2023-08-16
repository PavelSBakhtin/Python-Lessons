# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Square:

    def __init__(self, a, b=None):
        self.a = a
        self.b = b
        if b is None:
            self.b = a
        # self.a = a
        # if b is None:
        #     self.b = a
        # else:
        #     self.b = b

    def get_square(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * (self.a + self.b)


a, b = map(int, input('Введите стороны A и B через пробел: ').split())
sq = Square(a, b)
print(f'Площадь: {sq.get_square()}\nПериметр: {sq.get_perimetr()}')
