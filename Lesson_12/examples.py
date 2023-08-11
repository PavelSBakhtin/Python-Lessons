# # Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# # Экземпляр должен запоминать последние k значений.
# # Параметр k передаётся при создании экземпляра.
# # Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

# class Factorial:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._arg_archive = []
#             cls._instance._number_archive = []
#             cls._instance._factorial = 1
#         return cls._instance

#     def __call__(self, num):
#         self._arg_archive.append(num)
#         self.num = num
#         factorial = 1
#         for i in range(num):
#             factorial *= (i + 1)
#         self._number_archive.append(factorial)
#         return factorial


#     def __str__(self):
#         return f'{self._arg_archive}, {self._number_archive}'

#     def number_archive(self):
#         return self._arg_archive, self._number_archive


# fac = Factorial()

# print(fac(3))
# print(fac(4))
# print(fac(5))
# print(fac.number_archive())

# ###

# class Factorial:

#     def __init__(self):
#         self._arg_archive = []
#         self._number_archive = []
#         self._factorial = 1

#     def __call__(self, num):
#         self._arg_archive.append(num)
#         self.num = num
#         factorial = 1
#         for i in range(num):
#             factorial *= (i + 1)
#         self._number_archive.append(factorial)
#         return factorial


#     def __str__(self):
#         return f'{self._arg_archive}, {self._number_archive}'

#     def number_archive(self):
#         return self._arg_archive, self._number_archive


# fac = Factorial()
# fac1 = Factorial()

# print(fac(3))
# print(fac1(4))
# print(fac1(5))
# print(fac.number_archive())
# print(fac1.number_archive())

# # Доработаем задачу 1.
# # Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

# class Factorial:

#     def __init__(self):
#         self._arg_archive = []
#         self._number_archive = []
#         self._factorial = 1

#     def __call__(self, num):
#         self._arg_archive.append(num)
#         self.num = num
#         factorial = 1
#         for i in range(num):
#             factorial *= (i + 1)
#         self._number_archive.append(factorial)
#         return factorial


#     def __str__(self):
#         return f'{self._arg_archive}, {self._number_archive}'

#     def number_archive(self):
#         return self._arg_archive, self._number_archive

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.res = dict(zip(self._arg_archive, self._number_archive))
#         self.json_file = open('file.json', 'w')
#         json.dump(self.res, self.json_file, indent=2)
#         self.json_file.close()

# fac = Factorial()
# fac1 = Factorial()

# print(fac(3))
# print(fac1(4))
# print(fac1(5))
# print(fac.number_archive())
# print(fac1.number_archive())

# jw = Factorial()
# with jw as cm:
#     cm(5)

# # Создайте класс-генератор.
# # Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# # Если переданы два параметра, считаем step=1.
# # Если передан один параметр, также считаем start=1.

# class Factorial:
#     def __init__(self, start, stop = None, step = 1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         if stop is None:
#             self.stop = start
#             self.start = 1
#         self.value = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start <= self.stop:
#             self.value *= self.start
#             self.start += self.step
#             return self.value
#         raise StopIteration

# factorial = Factorial(1, 7)

# print(*factorial)

# # Доработайте класс прямоугольник из прошлых семинаров.
# # Добавьте возможность изменять длину и ширину прямоугольника
# # и встройте контроль недопустимых значений (отрицательных).
# # Используйте декораторы свойств.

# class Square:
    
#     def __init__(self, a, b):
#         self._a = a
#         if b is None:
#             self._b = a
#         else:
#             self._b = b
            
#     def __add__(self, other):
#         if isinstance(other, Square):
#             return Square(self._a + other._a, self._b + other._b)
#         return NotImplemented
    
#     def __sub__(self, other):
#         if isinstance(other, Square):
#             if other._a > self._a  or other._b > self._b:
#                 raise ValueError('Такой прямоугольник невозможен')
#             return Square(self._a - other._a, self._b - other._b)
#         return NotImplemented

#     def get_area(self):
#         return self._a * self._b

#     def get_perimetr(self):
#         return 2 * (self._a + self._b)
    
#     def __repr__(self):
#         return f"Square({self._a}, {self._b})"
    
#     @property
#     def a(self):
#         return self._a
    
#     @a.setter
#     def a(self, value):
#         if value > 0:
#             self._a = value
#         else:
#             raise ValueError('ПНХ')
    
#     @property
#     def b(self):
#         return self._b
    
#     @b.setter
#     def b(self, value):
#         if value > 0:
#             self._b = value
#         else:
#             raise ValueError('ПНХ')
    

# obj_a = Square(5, 6)
# print(obj_a)
# obj_a.a = 10
# print(obj_a)
# try:
#     obj_a.b = -10
# except ValueError as e:
#     print(e)

# # Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

# __slots__ = ('_a', '_b')

# # Изменяем класс прямоугольника.
# # Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

# class Range:

#     def __init__(self, min_value=None, max_value=None):
#         self.min_value = min_value
#         self.max_value = max_value

#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)

#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)

#     def validate(self, value):
#         if self.min_value is None or value < self.min_value:
#             raise ValueError('Ошибка!!!')
#         if self.max_value is None or value > self.max_value:
#             raise ValueError('Ошибка!!!')

# class Square:
#     _a = Range(0, 100)
#     _b = Range(0, 100)

#     def __init__(self, a, b):
#         self._a = a
#         if b is None:
#             self._b = a
#         else:
#             self._b = b

#     def __add__(self, other):
#         if isinstance(other, Square):
#             return Square(self._a + other._a, self._b + other._b)
#         return NotImplemented

#     def __sub__(self, other):
#         if isinstance(other, Square):
#             if other._a > self._a or other._b > self._b:
#                 raise ValueError('Такой прямоугольник невозможен')
#             return Square(self._a - other._a, self._b - other._b)
#         return NotImplemented

#     def get_area(self):
#         return self._a * self._b

#     def get_perimetr(self):
#         return 2 * (self._a + self._b)

#     def __repr__(self):
#         return f"Square({self._a}, {self._b})"

#     @property
#     def a(self):
#         return self._a

#     @a.setter
#     def a(self, value):
#         if value > 0:
#             self._a = value
#         else:
#             raise ValueError('ПНХ')

#     @property
#     def b(self):
#         return self._b

#     @b.setter
#     def b(self, value):
#         if value > 0:
#             self._b = value
#         else:
#             raise ValueError('ПНХ')


# obj_a = Square(5, 100)
# print(obj_a)
# obj_a.a = 10
# print(obj_a)
