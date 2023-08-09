# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle
import shutil
import os


def pickle_to_csv(file):
    path = os.getcwd()
    with open(file, 'rb') as f1, \
            open(f'{file[:-8]}6.csv', 'w', newline='') as f2:
        data = pickle.load(f1)
        head = data.keys()
        writer = csv.writer(f2, delimiter=';')
        writer.writerow(head)
        for key, value in data.items():
            a, b = tuple(*value.values())
            writer.writerow([*(value.keys()), a, b])
    f3 = f'{file[:-8]}6.csv'
    shutil.move(f3, path)


pickle_to_csv('lesson8_task5/lesson8_task4.pickle')
