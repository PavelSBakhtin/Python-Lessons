# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging

logging.basicConfig(level=logging.INFO, filename='loger.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')

x, y = map(int, input('Введите два целых числа через пробел: ').split())


def log_deco(func):
    def wrapper(x, y):
        try:
            logging.info(f'Result: {x} / {y} = {func(x, y)}')
        except:
            logging.error('ZeroDivisionZero')
    return wrapper


@log_deco
def log_div(x, y):
    return (x / y)


log_div(x, y)
