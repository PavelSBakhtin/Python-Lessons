# import time
# from getpass import getuser


# class MyString(str):
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls, *args, **kwargs)
#         instance.name = getuser()
#         instance.time_val = time.time()
#         return instance

#     def __init__(self, str_val):
#         self.str_val = str_val


# a = MyString('Hello world')
# print(a, a.name, a.time_val)


# class Archive:
#     _instance = None

#     def __new__(cls, string, number):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._string_archive = []
#             cls._instance._number_archive = []
#         else:
#             cls._instance._string_archive.append(cls._instance.string)
#             cls._instance._number_archive.append(cls._instance.number)
#         return cls._instance

#     def __init__(self, string, number):
#         self.string = string
#         self.number = number

#     def __str__(self):
#         return f"{self.number, self.string}"


#     def string_archive(self):
#         return self._string_archive


#     def number_archive(self):
#         return self._number_archive


# first = Archive('a', 1)
# second = Archive('b', 2)
# print(first.number_archive(), second)

# print(first.string_archive(), first.number_archive())

# third = Archive('c', 3)
# print(third.string_archive(), third.number_archive())

# print(third)


# class Archive:
#     """Это наш запрещенный класс!!!11 один один"""
#     _instance = None

#     def __new__(cls, string, number):
#         """
#         Это создание потомка
#         :param string: Это в архив строк
#         :param number: Это в архив чисел
#         """
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._string_archive = []
#             cls._instance._number_archive = []
#         else:
#             cls._instance._string_archive.append(cls._instance.string)
#             cls._instance._number_archive.append(cls._instance.number)
#         return cls._instance

#     def __init__(self, string, number):
#         """
#         Создание экземпляра класса
#         :param string: Это в архив строк
#         :param number: Это в архив чисел
#         """
#         self.string = string
#         self.number = number

#     def __str__(self):
#         """
#         Переопределение метода str
#         :return: Строка с данными
#         """
#         return f"{self.number, self.string}"

#     def __repr__(self):
#         """
#         Данные программисту
#         :return: Данные
#         """
#         return f'Archive({self.string.__repr__()}, {self.number})'

#     def string_archive(self):
#         """
#         Архивация строк
#         :return: Архив строк
#         """
#         return self._string_archive

#     def number_archive(self):
#         """
#         Архивация чисел
#         :return: Архив чисел
#         """
#         return self._number_archive


# first = Archive('a', 1)
# second = Archive('b', 2)
# print(first.number_archive(), second)
# print(first.string_archive(), first.number_archive())
# third = Archive('c', 3)
# print(third.string_archive(), third.number_archive())
# print(third.__repr__())
# print(my_list := [first, second, third])
# for item in my_list:
#     print(item)

# d = eval(third.__repr__())
# print(d)



# from functools import total_ordering

# @total_ordering
# class Square:
    
#     def __init__(self, a, b):
#         self.a = a
#         if b is None:
#             self.b = a
#         else:
#             self.b = b
            
#     def __add__(self, other):
#         if isinstance(other, Square):
#             return Square(self.a + other.a, self.b + other.b)
#         return NotImplemented
    
#     def __sub__(self, other):
#         if isinstance(other, Square):
#             if other.a > self.a  or other.b > self.b:
#                 raise ValueError('Такой прямоугольник невозможен')
#             return Square(self.a - other.a, self.b - other.b)
#         return NotImplemented

#     def get_area(self):
#         return self.a * self.b

#     def get_perimetr(self):
#         return 2 * (self.a + self.b)
    
#     def __repr__(self):
#         return f"Square({self.a}, {self.b})"
    
#     def __eq__(self, other):
#         if isinstance(other, Square):
#             return self.get_area() == other.get_area() 
#         return NotImplemented
    
#     def __gt__(self, other):
#         if isinstance(other, Square):
#             return self.get_area() > other.get_area()
#         return NotImplemented     

#     # def __ge__(self, other):
#     #     if isinstance(other, Square):
#     #         return self.get_area() >= other.get_area()
#     #     return NotImplemented          
  
# square_1 = Square(3, 4)
# square_2 = Square(5, 6)

# square_3 = square_1 + square_2
# square_4 = square_2 - square_1

# print(f"{square_1} + {square_2} = {square_3}")
# print(f"{square_2} - {square_1} = {square_4}")

# print(square_1 > square_2)
# print(square_1 < square_2)
# print(square_1 >= square_2)
# print(square_1 <= square_2)
# print(square_1 == square_2)
# print(square_1 != square_2)



