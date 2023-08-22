# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')

x, y = map(int, input('Введите два целых числа через пробел: ').split())
try:
    print((x / y))
    logging.info('Ok')
except:
    logging.error('ZeroDivisionZero')
