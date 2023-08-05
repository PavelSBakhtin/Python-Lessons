# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from lesson7_task5 import make_file
import os


def replace_file():
    for file in os.listdir():
        exception = file.split('.')[-1]
        if not os.path.exists(exception):
            os.mkdir(exception)
        os.replace(file, os.path.join(os.getcwd(), exception, file))


data = {'jpg': 5, 'bmp': 4, 'png': 3}
make_file(**data)
# replace_file()
