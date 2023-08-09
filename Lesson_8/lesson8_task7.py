# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle


def csv_to_json(file):
    with open(file, 'r', newline='') as f:
        csv_file = csv.reader(f, delimiter=';')
        count = 0
        values = []
        for line in csv_file:
            if count == 0:
                graphs = line
                count += 1
            else:
                values.append(line)
        dict_to_print = {}
        item = 0
        for key in graphs:
            dict_to_print[key] = values[item]
            item += 1
    print(f'{dict_to_print}\n')
    result = pickle.dumps(dict_to_print, protocol=pickle.DEFAULT_PROTOCOL)
    print(f'{result = }')


csv_to_json('lesson8_task6.csv')
