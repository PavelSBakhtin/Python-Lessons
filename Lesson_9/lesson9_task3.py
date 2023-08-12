# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json


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


@json_saver
def lesson9_task3(a, b, c='5'):
    return max(a, b, c)


print(lesson9_task3(2, 4, c=9))
