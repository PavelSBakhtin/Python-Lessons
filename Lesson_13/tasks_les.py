# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.


def input_float():
    try:
        return float(input('Enter float number -> '))
    except ValueError:
        print('Invalid value, expected float number through dot("."): ')
        return input_float()


def get_num():
    while True:
        try:
            num = float(input('Введите число: '))
            if num - int(num) == 0:
                num = int(num)
                # is_integer()
            break
        except ValueError:
            print('Ошибка ввода!')
    return num


print(get_num())


# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


my_dict = {'1': 2, '2': 4}


def dict_get(inp_dict: dict, key=None, value=None):
    try:
        return inp_dict[key]
    except:
        return value


print(my_dict)
print(dict_get(my_dict, '1'))
print(dict_get(my_dict, '3', 5))


# Создайте класс с базовым исключением и дочерние классы-исключения:
# - ошибка уровня,
# - ошибка доступа.


class UserException(Exception):
    pass

class UserLevelError(UserException):
    pass

class UserPermissionError(UserException):
    pass


raise UserLevelError


# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла
# и формирует множество пользователей.


import json
import os.path


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
        self.json_data = {self.firstname: [lastname, sex, age, self.lvl_id, pers_id]}
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
        except:
            return 'Ошибка записи!'


def user_create():
    user_list = []
    with open('json_file.json', 'r') as f_read:
        data = json.load(f_read)
    for firstname, values in data.items():
        lastname, sex, age, lvl_id, pers_id = values
        user_list.append(Employee(firstname, lastname, sex, age, pers_id))
    return user_list


e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
e2 = Employee('Петя', 'Петров', 'М', 25, '654321')
e3 = Employee('Глафира', 'Вениаминовна', 'Ж', 41, '333555')

# print(e1)
# print(e2)
# print(e3)

print(*user_create())


# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# - загрузка данных (функция из задания 4);
# - вход в систему - требует указать имя и id пользователя;
#   для проверки наличия пользователя в множестве используйте
#   магический метод проверки на равенство пользователей;
#   если такого пользователя нет, вызывайте исключение доступа;
#   а если пользователь есть, получите его уровень из множества пользователей;
# - добавление пользователя; если уровень пользователя меньше, чем ваш уровень,
#   вызывайте исключение уровня доступа.


import json
import os.path


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
        self.json_data = {self.firstname: [lastname, sex, age, self.lvl_id, pers_id]}
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
        except:
            return 'Ошибка записи!'


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


class Login():
    def user_login(self, user_name, user_id):
        try:
            with open('json_file.json', 'r') as f_read:
                data = json.load(f_read)
            for firstname, values in data.items():
                lastname, sex, age, lvl_id, pers_id = values
                curr_user = Employee(firstname, lastname, sex, age, pers_id)
                if firstname == user_name and pers_id == user_id:
                    user_from_base = Employee(firstname, lastname, sex, age, pers_id)
                    return curr_user.lvl_id
        except:
            raise UserPermissionError

    def user_creator(self, data, creator_lvl):
        new_user = Employee(*data)
        print(data)
        print(new_user)
        if new_user.lvl_id >= creator_lvl:
            return new_user
        else:
            raise UserLevelError


e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
e2 = Employee('Петя', 'Петров', 'М', 25, '654321')
e3 = Employee('Глафира', 'Вениаминовна', 'Ж', 41, '999999')
e4 = ('Антон', 'Анатольевич', 'М', 24, '123456')


us1 = Login()
print(us1.user_creator(e4, us1.user_login('Глафира', '999999')))


# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.





