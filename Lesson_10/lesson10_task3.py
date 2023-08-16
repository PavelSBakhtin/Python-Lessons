# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

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


p1 = Person('Вася', 'Иванов', 'М', 30)

print(p1.get_age())
print(p1.birthday())
print(p1.get_age())
print(p1.full_name())
print(p1._Person__age)
print(p1.__age) # прямое обращение выдаст ошибку
