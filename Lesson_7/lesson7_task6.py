# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from lesson7_task4 import create_file
import os


def create_to_path(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    create_file(extention)


create_to_path('lesson7_task6', 'mp3')
