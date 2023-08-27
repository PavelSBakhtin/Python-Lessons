# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# - загрузка данных (функция из задания 4);
# - вход в систему - требует указать имя и id пользователя;
#   для проверки наличия пользователя в множестве используйте
#   магический метод проверки на равенство пользователей;
#   если такого пользователя нет, вызывайте исключение доступа;
#   а если пользователь есть, получите его уровень из множества пользователей;
# - добавление пользователя; если уровень пользователя меньше, чем ваш уровень,
#   вызывайте исключение уровня доступа.

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
    with open(f'Lesson_13/task5_{company}.json', 'w', encoding='utf-8') as file:
        json.dump(employees, file, sort_keys=True, indent=4, ensure_ascii=False)
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


class UserException(Exception):
    
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class UserLevelError(UserException):
    
    def __init__(self, me, new):
        super(UserLevelError, self).__init__(f'Ошибка уровня доступа: сотрудник {me.employee_name} с уровнем доступа {me.level_access} - не имеет прав\n'
                                             f'на создание нового сотрудника {new.employee_name} с уровнем доступа {new.level_access}, который меньше вашего')


class UserAccessError(UserException):
    
    def __init__(self, me: Employee):
        super(UserAccessError, self).__init__(f'Ошибка доступа: сотрудник {me.employee_name} с id {me.employee_id} не зарегистрирован')


class UserUniqueID(UserException):

    def __init__(self, new_id: str):
        super(UserUniqueID, self).__init__(f'Ошибка записи: сотрудник с id - {new_id} уже существует')


class Company:

    def __init__(self, с_name):
        self.name = с_name
        if os.path.exists(f'Lesson_13/task5_{self.name}.json'):
            with open(f'Lesson_13/task5_{self.name}.json', 'r', encoding='utf-8') as file:
                employees_list = json.load(file)
        else:
            employees_list = add_employee(self.name, 10)
        self.employees = [Employee(e_name, e_level, e_id)
                          for e_level, person in employees_list.items()
                          for e_id, e_name in person.items()]

    def login(self, e_name: str, e_id: str):
        for employee in self.employees:
            if employee.employee_name == e_name and employee.employee_id == e_id:
                return employee
        raise UserAccessError(Employee(e_name, 7, e_id))

    def hiring(self, me: Employee, new_name: str, new_id: str, new_level: int):
        if me:
            if me.level_access < new_level:
                if new_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(new_name, int(new_level), new_id))
                    self.__save()
                else:
                    raise UserUniqueID(new_id)
            else:
                raise UserLevelError(me, Employee(new_name, new_level, new_id))
        else:
            raise UserAccessError(Employee(me))

    def __save(self):
        employees_update = {}
        for employee in self.employees:
            if employee.level_access in employees_update:
                employees_update[employee.level_access][employee.employee_id] = employee.employee_name
            else:
                employees_update[employee.level_access] = {employee.employee_id: employee.employee_name}
        with open(f'Lesson_13/task5_{self.name}.json', 'w', encoding='utf-8') as file:
            json.dump(employees_update, file, sort_keys=True, indent=4, ensure_ascii=False)


nykis = Company('nykis')
me = nykis.login('Вася Василич Васин', '353454')
nykis.hiring(me, 'Колян Николаевич Колин', '360132', 1)
