# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.

from functools import total_ordering


@total_ordering
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

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.get_area() == other.get_area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.get_area() > other.get_area()
        return NotImplemented

    # # Это используется, если нет декоратора @total_ordering:
    # def __ge__(self, other):
    #     if isinstance(other, Square):
    #         return self.get_area() >= other.get_area()
    #     return NotImplemented


square_1 = Square(3, 4)
square_2 = Square(5, 6)

square_3 = square_1 + square_2
square_4 = square_2 - square_1

print(f'{square_1} + {square_2} = {square_3}')
print(f'{square_2} - {square_1} = {square_4}')

print(square_1 > square_2)
print(square_1 < square_2)
print(square_1 >= square_2)
print(square_1 <= square_2)
print(square_1 == square_2)
print(square_1 != square_2)
