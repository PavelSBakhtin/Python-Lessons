# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def numbers(lines, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(lines):
            file.write(
                f'{randint(-1000, 1000)} | {round(uniform(-1000, 1000), 3)}\n')


def input_mode():
    n = int(input('Select input mode number of lines - manual (1), random (2): '))
    if n == 1:
        numbers(int(input('Enter the number of lines: ')), 'lesson7_task1.txt')
    elif n == 2:
        numbers(randint(1, 5), 'lesson7_task1.txt')
    else:
        print('Wrong number')


input_mode()
