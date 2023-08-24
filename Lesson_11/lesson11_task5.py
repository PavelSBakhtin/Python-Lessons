# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Square:

    def __init__(self, a, b):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self.a + other.a, self.b + other.b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other.a > self.a or other.b > self.b:
                raise ValueError('Такой прямоугольник невозможен')
            return Square(self.a - other.a, self.b - other.b)
        return NotImplemented

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * (self.a + self.b)

    def __repr__(self):
        return f'Square({self.a}, {self.b})'


square_1 = Square(3, 4)
square_2 = Square(5, 6)

square_3 = square_1 + square_2
square_4 = square_2 - square_1

print(f'{square_1} + {square_2} = {square_3}')
print(f'{square_2} - {square_1} = {square_4}')
print(square_3.__repr__())
print(square_4.__repr__())
