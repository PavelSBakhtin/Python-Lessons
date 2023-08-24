# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json
import os.path
import pytest


class UserException(Exception):
    pass


class UserLevelError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка уровня! {self.value}'


class UserPermissionError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка доступа! {self.value}'


class Person:

    def __init__(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.firstname} {self.lastname} {self.sex}'

    def get_age(self):
        return self.__age


class Employee(Person):

    def __init__(self, firstname, lastname, sex, age, pers_id):
        if len(pers_id) != 6:
            raise ValueError('Некорректный id!')
        super().__init__(firstname, lastname, sex, age)
        self.pers_id = pers_id
        self.lvl_id = int(pers_id) % 7
        self.json_data = {self.firstname: [
            lastname, sex, age, self.lvl_id, pers_id]}
        self.save_in_files()

    def __str__(self):
        return f'{self.firstname}: уровень: {self.lvl_id}, ID: {self.pers_id}'

    def save_in_files(self):
        try:
            if not os.path.isfile('json_file.json') or os.path.getsize('json_file.json') == 0:
                with open('json_file.json', 'w') as f:
                    f.write('{}')
            with open('json_file.json', 'r') as f_read:
                data = json.load(f_read)
                data.update(self.json_data)
            with open('json_file.json', 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, ensure_ascii=False, indent=2)
        except SystemError as e:
            return f'Ошибка записи! Не удалось открыть файл.'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.pers_id == other.pers_id
        return NotImplemented


def user_create():
    user_list = []
    with open('json_file.json', 'r') as f_read:
        data = json.load(f_read)
    for firstname, values in data.items():
        lastname, sex, age, lvl_id, pers_id = values
        user_list.append(Employee(firstname, lastname, sex, age, pers_id))
    return user_list


class Login:

    def user_login(self, user_name, user_id):
        with open('json_file.json', 'r') as f_read:
            data = json.load(f_read)
            if user_name in data and data[user_name][4] == user_id:
                return int(data[user_name][3])
            else:
                raise UserPermissionError(user_id)

    def user_creator(self, data, creator_lvl):
        new_user = Employee(*data)
        if new_user.lvl_id <= creator_lvl:
            return new_user
        else:
            raise UserLevelError(creator_lvl)


@pytest.fixture
def data():
    e4 = ('Антон', 'Анатольевич', 'М', 24, '123456')
    us1 = Login()
    return [e4, us1]


def test_value_error():
    assert Employee('Вася', 'Иванов', 'М', 30, '123456')


def test_user_lvl_err(data):
    assert data[1].user_creator(data[0], data[1].user_login('Антон', '123456'))


def test_user_perm_err(data):
    assert data[1].user_login('Антон', '123456')


if __name__ == "__main__":
    pytest.main()
