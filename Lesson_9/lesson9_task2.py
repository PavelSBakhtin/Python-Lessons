# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint


def main(func):
    def wrapper(upper_limit, attempt):
        if not 0 < upper_limit < 100:
            upper_limit = randint(1, 100)
        if not 0 < attempt < 10:
            attempt = randint(1, 10)
        func(upper_limit, attempt)
    return wrapper


@main
def try_to_guess(upper_limit, attempt):
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
try_to_guess(upper_limit, attempt)
