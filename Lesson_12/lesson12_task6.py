# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.


class Range:

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if self.min_value is None or value < self.min_value:
            raise ValueError('Ошибка!!!')
        if self.max_value is None or value > self.max_value:
            raise ValueError('Ошибка!!!')


class Square:

    _a = Range(0, 100)
    _b = Range(0, 100)

    def __init__(self, a, b):
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self._a + other._a, self._b + other._b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other._a > self._a or other._b > self._b:
                raise ValueError('Такой прямоугольник невозможен')
            return Square(self._a - other._a, self._b - other._b)
        return NotImplemented

    def get_area(self):
        return self._a * self._b

    def get_perimetr(self):
        return 2 * (self._a + self._b)

    def __repr__(self):
        return f'Square({self._a}, {self._b})'

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('ПНХ')

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError('ПНХ')


obj_a = Square(5, 100)
print(obj_a)
obj_a.a = 10
print(obj_a)
