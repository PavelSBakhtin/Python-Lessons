# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# - расширение;
# - минимальная длина случайно сгенерированного имени, по умолчанию 6;
# - максимальная длина случайно сгенерированного имени, по умолчанию 30;
# - минимальное число случайных байт, записанных в файл, по умолчанию 256;
# - максимальное число случайных байт, записанных в файл, по умолчанию 4096;
# - количество файлов, по умолчанию 42.
# Имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_letters
from random import randint, sample
# from random import randbytes # для версий 3.9+


def randbytes_py38(min_bytes, max_bytes):
    ONE_BYTE = 128
    count = randint(min_bytes, max_bytes)
    res = bytes('', encoding='utf_8')
    for _ in range(count):
        bt = randint(0, ONE_BYTE)
        res += bytes(chr(bt), encoding='utf_8')
    return res


def create_file(extention, short=6, long=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    item = 1
    while len(names) < count:
        name = f'{item}' + ''.join(sample(ascii_letters, randint(short, long)))
        names.add(name)
        item += 1
    for i in names:
        size = randbytes_py38(min_bytes, max_bytes)
        with open(f'{i}.{extention}', 'wb') as file:
            file.write(size)


create_file('txt')


# def create_file(extention, short=6, long=30, min_bytes=256, max_bytes=4096, count=42):
#     names = set()
#     item = 1
#     while len(names) < count:
#         name = f'{item}' + ''.join(sample(ascii_letters, randint(short, long)))
#         names.add(name)
#         item += 1
#     for i in names:
#         with open(f'{i}.{extention}', 'wb', encoding='utf_8') as file:
#             file.write(randbytes(min_bytes, max_bytes))
