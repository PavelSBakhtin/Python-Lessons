# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.


class Archive:
    """Это наш запрещенный класс!!!"""
    _instance = None

    def __new__(cls, string, number):
        """
        Это создание потомка
        :param string: Это в архив строк
        :param number: Это в архив чисел
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._string_archive = []
            cls._instance._number_archive = []
        else:
            cls._instance._string_archive.append(cls._instance.string)
            cls._instance._number_archive.append(cls._instance.number)
        return cls._instance

    def __init__(self, string, number):
        """
        Создание экземпляра класса
        :param string: Это в архив строк
        :param number: Это в архив чисел
        """
        self.string = string
        self.number = number

    def __str__(self):
        """
        Переопределение метода str
        :return: Строка с данными
        """
        return f"{self.number, self.string}"

    def __repr__(self):
        """
        Данные программисту
        :return: Данные
        """
        return f'Archive({self.string.__repr__()}, {self.number})'

    def string_archive(self):
        """
        Архивация строк
        :return: Архив строк
        """
        return self._string_archive

    def number_archive(self):
        """
        Архивация чисел
        :return: Архив чисел
        """
        return self._number_archive


first = Archive('a', 1)
second = Archive('b', 2)
print(first.number_archive(), second)
print(first.string_archive(), first.number_archive())
third = Archive('c', 3)
print(third.string_archive(), third.number_archive())
print(third.__repr__())
print(my_list := [first, second, third])
for item in my_list:
    print(item)
d = eval(third.__repr__())
print(d)
