# Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle
import os
import shutil


def json_to_pickle(path):
    if not os.path.exists(path):
        os.mkdir(path)
    for file in os.listdir():
        if file.endswith('.json'):
            file_name, file_ext = file.rsplit('.')
            with open(file, 'r') as f1, \
                    open(f'{file_name}.pickle', 'wb') as f2:
                pickle.dump(json.load(f1), f2)
    for f in os.listdir():
        if f.endswith('.pickle'):
            shutil.move(f, path)


json_to_pickle('lesson8_task5')
