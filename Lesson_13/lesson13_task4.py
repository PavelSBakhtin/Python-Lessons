# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла
# и формирует множество пользователей.

import json


def level_json():
    while True:
        str_inp = input('Введите данные через пробел: ')
        if str_inp:
            name, pers_id, level = str_inp.split()
            if not 0 < int(level) < 8:
                print('Неверный уровень доступа')
                continue

            try:
                with open('Lesson_13/lesson13_task4.json', 'r') as f1:
                    data = json.load(f1)
            except:
                data = {}
                
            if level not in data:
                data[level] = {}
            data[level][pers_id] = name
            with open('Lesson_13/lesson13_task4.json', 'w') as f2:
                json.dump(data, f2, sort_keys=True, indent=4)
        else:
            break


level_json()
