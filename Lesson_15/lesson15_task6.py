# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# - имя файла без расширения или название каталога,
# - расширение, если это файл,
# - флаг каталога,
# - название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import locale
import logging
from collections import namedtuple
import os

locale.setlocale(locale.LC_ALL, "Russian")


logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')


def file_listening(path='.'):
    """
    Рекурсивно обходит заданный каталог и все вложенные директории
    """

    for dirpath, dir_name, file_name in os.walk(path):
        Files = namedtuple(
            'Files', ['item_name', 'file_ext', 'dir_flag', 'parent_path'])
        parent_path = dirpath.split('\\')[-2]

        if dir_name:
            dir_flag = 'Is a direcory.'
            exp_dict = Files(dir_name, None, dir_flag, parent_path)
            logging.info(f'{exp_dict}')

        if file_name:
            dir_flag = 'Is a file.'
            for f in file_name:
                exp_dict = Files(f.split('.')[0], f.split(
                    '.')[-1], dir_flag, parent_path)
                logging.info(f'{exp_dict}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сканер файлов.')
    parser.add_argument(
        'path', type=str, help='Введите путь: ', default=os.getcwd())
    args = parser.parse_args()
    print(file_listening(args.path))
