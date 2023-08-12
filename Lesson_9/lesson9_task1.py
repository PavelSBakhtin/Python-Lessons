# Создайте функцию-замыкание, которая запрашивает два целых числа:
# - от 1 до 100 для загадывания,
# - от 1 до 10 для количества попыток
# Функция возвращает функцию,
# которая через консоль просит угадать загаданное число за указанное число попыток.

from random import randint


def main():
    upper_limit, attempt = int(input('Укажите предел: ')), int(input('Количество попыток: '))

    def try_to_guess():
        lower_limit = 1
        number = randint(lower_limit, upper_limit)
        nonlocal attempt
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
    
    return try_to_guess


a = main()
a()
