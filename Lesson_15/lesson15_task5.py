# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# * Научите функцию распознавать не только текстовое названия дня недели и месяца,
# но и числовые, т.е не мая, а 5.

import argparse
import re
import locale
import logging
from datetime import date
from datetime import timedelta

locale.setlocale(locale.LC_ALL, "Russian")
logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')


def parse_date(string):
    string = ' '.join(string)
    try:
        weekdays = {
            'понедельник': 0,
            "вторник": 1,
            "среда": 2,
            "четверг": 3,
            "пятница": 4,
            "суббота": 5,
            "воскресенье": 6,
        }
        months = {'января': 1,
                  'февраля': 2,
                  'марта': 3,
                  'апреля': 4,
                  'мая': 5,
                  'июня': 6,
                  'июля': 7,
                  'августа': 8,
                  'сентября': 9,
                  'октября': 10,
                  'ноября': 11,
                  'декабря': 12
                  }

        day_no = int(re.findall(r'\d+', string)[0])
        _weekday = weekdays[string.split()[1]]
        _months = months[string.split()[2]]

        startdate = date(2023, _months, 1)
        weekday_count = 0
        while weekday_count < day_no:
            if startdate.weekday() == _weekday:
                weekday_count += 1
            startdate += timedelta(days=1)
        logging.info(startdate - timedelta(days=1))
        return startdate - timedelta(days=1)
    except Exception as e:
        logging.error(e)


# str_inp = '4-ый четверг ноября'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Логер даты.')
    parser.add_argument('-a', type=str, nargs=1,
                        help='Введите порядковый день недели', default=['1'])
    parser.add_argument('-b', type=str, nargs=1,
                        help='Текущий день недели', default=['вторник'])
    parser.add_argument('-c', type=str, nargs=1,
                        help='Текущий месяц', default=['августа'])
    args = parser.parse_args()
    args_list = args.a + args.b + args.c
    print(args_list)
    print(parse_date(args_list))
