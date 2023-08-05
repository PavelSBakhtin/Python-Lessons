# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from lesson7_task4 import create_file


def make_file(**extentions):
    for extention, count in extentions.items():
        create_file(extention=extention, count=count)


data = {'txt': 3, 'bmp': 4, 'png': 5}
make_file(**data)
