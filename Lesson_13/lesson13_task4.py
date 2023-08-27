# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла
# и формирует множество пользователей.

import os
import json
from random import randint
from faker import Faker


def add_employee(company: str, count: int):
    employees = {}
    list_id = []
    for _ in range(count):
        employee_name = Faker('ru_RU').name()
        while True:
            employee_id = str(randint(1, 999999)).zfill(6)
            if employee_id not in list_id:
                list_id.append(employee_id)
                break
        level_access = int(employee_id) % 7 + 1
        if level_access in employees:
            employees[level_access][employee_id] = employee_name
        else:
            employees[level_access] = {employee_id: employee_name}
    with open(f'Lesson_13/task4_{company}.json', 'w', encoding='utf-8') as file:
        json.dump(employees, file, sort_keys=True,
                  indent=4, ensure_ascii=False)
    return employees


class DescriptorName:

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value: str):
        if not all([all(list(map(lambda x: x.isalpha(), name))) for name in value.split()]):
            raise ValueError(f'Имя должно быть только из букв: {value}')
        if not all(map(lambda x: x.istitle(), value.split())):
            raise ValueError(f'ФИО должны быть с заглавных букв: {value}')
        setattr(instance, self._name, value)


class DescriptorID:

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value: str):
        if not len(value) == 6:
            raise ValueError(f'ID должен быть шестизначным: {value}')
        if not value.isdigit():
            raise ValueError(f'ID должен быть только из цифр: {value}')
        setattr(instance, self._name, value)


class Employee:

    employee_name = DescriptorName()
    employee_id = DescriptorID()

    def __init__(self, employee_name: str, level_access: int, employee_id: str):
        self.employee_name = employee_name
        self.employee_id = employee_id
        if 0 < int(level_access) < 8:
            self.level_access = int(level_access)
        else:
            raise ValueError(f'Уровень доступа должен быть от 1 до 7: {level_access}')

    def __str__(self):
        return f'{self.employee_name} ({self.employee_id}) | доступ: {self.level_access}'

    def __eq__(self, other):
        return self.employee_name == other.employee_name and self.employee_id == other.employee_id


class Company:

    def __init__(self, с_name):
        self.name = с_name
        if os.path.exists(f'Lesson_13/task4_{self.name}.json'):
            with open(f'Lesson_13/task4_{self.name}.json', 'r', encoding='utf-8') as file:
                employees_list = json.load(file)
        else:
            employees_list = add_employee(self.name, 10)
        self.employees = [Employee(e_name, e_level, e_id)
                          for e_level, person in employees_list.items()
                          for e_id, e_name in person.items()]
        

abibas = Company('abibas')
belibok = Company('belibok')
print(*abibas.employees, sep='\n')
print(*belibok.employees, sep='\n')
