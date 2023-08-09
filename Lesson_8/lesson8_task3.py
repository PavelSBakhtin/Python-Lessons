# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv


def json_to_csv():
    with open('lesson8_task2.json', 'r') as f1, \
            open('lesson8_task3.csv', 'w', newline='', encoding='utf-8') as f2:
        data = json.load(f1)
        columns = ['level', 'pers_id', 'name']
        csv_write = csv.writer(f2, delimiter=';')
        csv_write.writerow(columns)
        result = []
        for key, value in data.items():
            for i in value:
                result.append([key, i, data[key][i]])
        csv_write.writerows(result)


json_to_csv()
