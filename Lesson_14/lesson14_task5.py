# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую
# периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import io
import unittest
from unittest.mock import patch


class Rect:

    def __init__(self, a, b):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b
        self.validate()

    def validate(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError('Ошибка!!! Значение должно быть больше нуля!')

    def __add__(self, other):
        if isinstance(other, Rect):
            return Rect(self.a + other.a, self.b + other.b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rect):
            if other.a > self.a or other.b > self.b:
                raise ValueError('Такой прямоугольник невозможен')
            return Rect(self.a - other.a, self.b - other.b)
        return NotImplemented

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * (self.a + self.b)

    def __repr__(self):
        return f"Square({self.a}, {self.b})"


class Other:
    pass


class TestRect(unittest.TestCase):
    
    def test_value_error(self):
        with self.assertRaises(ValueError):
            Rect(0, 5)

    def test_type_error_add(self):
        with self.assertRaises(TypeError):
            Rect(4, 5) + Other

    def test_type_error_sub(self):
        with self.assertRaises(TypeError):
            Rect(4, 5) - Other

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fail_rect(self, mock_stdout):
        with self.assertRaises(ValueError):
            Rect(1, 1) - Rect(5, 5)
            self.assertEquals(mock_stdout.getvalue(),
                              'Такой прямоугольник невозможен')


if __name__ == "__main__":
    unittest.main()
