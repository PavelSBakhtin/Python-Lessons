# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# - шестизначный идентификационный номер;
# - уровень доступа вычисляемый как остаток от деления суммы цифр id на семь.


class Person:

    def __init__(self, firs_tname, last_name, sex, age):
        self.first_name = firs_tname
        self.last_name = last_name
        self.sex = sex
        self.__age = age

    def birthday(self):
        self.__age += 1
        return f'Возраст для {self.first_name} увеличен на 1 год'

    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.sex}'

    def get_age(self):
        return self.__age


class Employee(Person):

    def __init__(self, first_name, last_name, sex, age, id):
        if len(id) != 6:
            raise ValueError('Некорректный id')
        super().__init__(first_name, last_name, sex, age)
        self.id = id
        self.level = int(id) % 7

    def __str__(self):
        return f'{self.first_name}: уровень - {self.level}, id - {self.id}'


e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
print(e1)


# # вместо декоратора проще использовать __str__ в классе:
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
