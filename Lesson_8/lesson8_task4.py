# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл,
# где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
import csv


def csv_to_json(file_org, file_fin):
    with open(file_org, 'r', newline='') as f1, \
            open(file_fin, 'w', encoding='utf-8') as f2:
        csv_file = csv.reader(f1, delimiter=';')
        next(csv_file)
        dict_to_save = {}
        for level, pers_id, name in csv_file:
            pers_id = pers_id.rjust(10, '0')
            name = name.title()
            hash_id = hash(name + pers_id)
            dict_to_save[hash_id] = {level: [pers_id, name]}
        json.dump(dict_to_save, f2, indent=2)


csv_to_json('lesson8_task3.csv', 'lesson8_task4.json')
