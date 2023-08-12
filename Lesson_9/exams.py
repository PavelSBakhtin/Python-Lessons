# def json_saver(func):
#     def wrapper(*args, **kwargs):
#         with open(f'{func.__name__}.json', 'a') as file:
#             temp_dict = {'args' : args}
#             temp_dict.update(kwargs)
#             result = func(*args, **kwargs)
#             temp_dict['result'] =  result
#             json.dump(temp_dict, file, indent=3, ensure_ascii=False)
#         return result
#     return wrapper


# with open('example.json', 'r') as file:
#     data = json.load(file)
#     print(data)


# def counter(func):
#     def wrapper(count):
#         for i in range(count):
#             func()
#     return wrapper

# @counter
# def printer():
#     print("data")

# printer(5)





# def input_checker(func):
#     def wrapper():
#         upper_limit, find_try = map(int, (input('Введите лимит числа и количество угадывания: ').split()))
#         if not (0 < upper_limit < 100 or 0 < find_try < 10):
#             upper_limit = randint(1, 100)
#             find_try = randint(1, 10)
#             print('Числа вне диапазона')
#         func(upper_limit, find_try)
#     return wrapper

# @main
# def try_to_guess(upper_limit, find_try):
#     num = randint(1, upper_limit)
#     print(f'Угадай число от 1 до {upper_limit}.\n')
#     tmp = find_try
#     while find_try > 0:
#         guess_try = int(input('Введи число: '))
#         find_try -= 1
#         if guess_try < num:
#             print('У меня больше.')
#         if guess_try > num:
#             print('У меня меньше.')
#         if guess_try == num:
#             print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
#     else:
#         print(f'\nНе угадал! Я загадал {num}.')


# @call_count(3)
# @value_control
# @json_saver
# def try_to_guess(upper_limit, find_try):
#     num = randint(1, upper_limit)
#     print(f'Угадай число от 1 до {upper_limit}.\n')
#     tmp = find_try
#     while find_try > 0:
#         guess_try = int(input('Введи число: '))
#         find_try -= 1
#         if guess_try < num:
#             print('У меня больше.')
#         if guess_try > num:
#             print('У меня меньше.')
#         if guess_try == num:
#             print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
#     else:
#         print(f'\nНе угадал! Я загадал {num}.')

# try_to_guess(50, 3)
