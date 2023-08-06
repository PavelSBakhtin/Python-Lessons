# Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json


def level_json():
    while True:
        str_inp = input('Введите данные через пробел: ')
        if str_inp:
            name, pers_id, level = str_inp.split()
            if not 0 < int(level) < 8:
                print('Неверный уровень доступа')
                continue
            with open('lesson8_task2.json', 'r') as f1:
                try:
                    data = json.load(f1)
                except:
                    data = {}
            if level not in data:
                data[level] = {}
            data[level][pers_id] = name
            with open('lesson8_task2.json', 'w') as f2:
                json.dump(data, f2, sort_keys=True)
        else:
            break


level_json()
