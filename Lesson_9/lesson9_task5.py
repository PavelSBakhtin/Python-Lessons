# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# - декораторами для сохранения параметров,
# - декоратором контроля значений и
# - декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from random import randint
import json


def value_control(func):
    def wrapper(upper_limit, attempt):
        if not 0 < upper_limit < 100:
            upper_limit = randint(1, 100)
        if not 0 < attempt < 10:
            attempt = randint(1, 10)
        func(upper_limit, attempt)
    return wrapper


def json_saver(func):
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}.json', 'r') as f1:
            try:
                data = json.load(f1)
            except:
                data = {1: None}
        with open(f'{func.__name__}.json', 'w') as f2:
            if max(data.keys()) != 1:
                key = int(max(data.keys())) + 1
            else:
                key = max(data.keys())
            temp_dict = {'args': args}
            temp_dict.update(kwargs)
            result = func(*args, **kwargs)
            temp_dict['result'] = result
            data[key] = temp_dict
            json.dump(data, f2, indent=2, ensure_ascii=False)
        return result
    return wrapper


def call_count(num):
    def decorator(func):
        result = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return decorator


@call_count(1)
@value_control
@json_saver
def lesson9_task5(upper_limit, attempt):
    lower_limit = 1
    number = randint(lower_limit, upper_limit)
    print('Вы попали в игру - Угадай число!\nУ вас есть {} попыток'.format(attempt))
    win = False

    while attempt > 0:
        num = int(input('Введите число от 1 до {}: '.format(upper_limit)))
        if num > number:
            print('Загаданное число меньше')
            attempt -= 1
        elif num < number:
            print('Загаданное число больше')
            attempt -= 1
        else:
            print('Загаданное число угадано')
            win = True
            break
        print('Осталось попыток: ', attempt)

    if win:
        print('Вы выйграли!\nНе использовано попыток: {}'.format(attempt - 1))
    else:
        print('Вы проиграли...\nЗагаданное число: {}'.format(number))


upper_limit, attempt = int(input('Укажите предел: ')),int(input('Количество попыток: '))
lesson9_task5(upper_limit, attempt)
