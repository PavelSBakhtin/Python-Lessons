# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
from math import pi

# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return pi*self.radius**2

#     def get_perimetr(self):
#         return 2*pi*self.radius

# radius = 1
# circle = Circle(radius)
# print(f"{circle.get_area()}, {circle.get_perimetr()}")


# self.a = a
# self.b = b
# if b is None:
# self.b = a

# class Square:

#     def __init__(self, a, b=None):
#         self.a = a
#         if b is None:
#             self.b = a
#         else:
#             self.b = b

#     def get_area(self):
#         return self.a * self.b

#     def get_perimetr(self):
#         return 2 * (self.a + self.b)


# sq1 = Square(3, 4)
# print(sq1.get_area(), sq1.get_perimetr())


# class Person:

#     def __init__(self, firstname, lastname, sex, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.sex = sex
#         self.__age = age

#     def birthday(self):
#         self.__age += 1

#     def full_name(self):
#         return f'{self.firstname} {self.lastname} {self.sex}'

#     def get_age(self):
#         return self.__age


# p1 = Person('Вася', 'Иванов', 'М', 30)

# print(p1.get_age())
# print(p1.birthday())
# print(p1.get_age())
# print(p1.full_name())
# print(p1._Person__age)
# print(p1.__age)


import functools

# def auto_repr(args, kwargs):
#     def decorator(cls):
        
#         def custom_repr(cls):
#             args_list = [repr(cls.__getattribute__(i)) for i in args]
#             kwargs_list = [f"{i}={repr(cls.__getattribute__(i))}" for i in kwargs]
#             result = f"{cls.__class__.__name__}({', '.join(args_list + kwargs_list)})"
#             return result
           
#         cls.__repr__ = custom_repr
#         return cls
#     return decorator

# class Employee(Person):

#     def __init__(self, firstname, lastname, sex, age, pers_id):
#         if len(pers_id) != 6:
#             raise ValueError('Некорректный id!')
#         super().__init__(firstname, lastname, sex, age)
#         self.pers_id = pers_id
#         self.lvl_id = int(pers_id) % 7


#     def __str__(self):
#         return f'{self.firstname}: уровень: {self.lvl_id}, ID: {self.pers_id}'


# e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
# print(e1)



# class Animal:
#     def __init__(self, name, age, voice = 'groal'):
#         self.name = name
#         self.age = age
#         self.voice = voice
    
#     def make_voice(self):
#         print(self.voice)



# class Fish(Animal):
#     def __init__(self, name, age, scales, voice):
#         super().__init__(name, age, voice)      
#         self.scales = scales


#     def swim(self):
#         print("i'm swimming, oh, it's titan!")


# class Dog(Animal):
#     def __init__(self, name, age, breed, voice):
#         super().__init__(name, age, voice)  
#         self.breed = breed

#     def bark(self):
#         print('Bark!')


# class Raven(Animal):
#     def __init__(self, name, age, color, voice):
#         super().__init__(name, age)
#         self.voice = voice
#         self.color = name
    
#     def fly_around_corpse(self):
#         print('oooh, meat....')

# fish = Fish('Nemo', 2, 'silver', 'bul-bul')
# dog = Dog('Spark', 5, 'pitbull', 'bark!')
# bird = Raven('Qarasique', 6, 'white', 'bravo!')

# animals = [fish, dog, bird]

# for i in animals:
#     i.make_voice()

# fish.swim()
# dog.bark()
# bird.fly_around_corpse()
