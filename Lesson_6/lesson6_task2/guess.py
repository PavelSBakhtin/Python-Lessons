from random import randint


def guess_num(lower, upper, attempts):
    num = randint(lower, upper)
    # два варианта оформления формата
    print(f'Угадай число от {lower} до {upper}:\n')
    # print('Угадай число от {0} до {1}:\n'.format(lower, upper))

    count = 0
    while attempts > 0:
        attempt = int(input('Введите число: '))
        attempts -= 1
        count += 1
        if attempt < num:
            print('Загадано число больше')
        if attempt > num:
            print('Загадано число меньше')
        if attempt == num:
            print(f'Победа! Угадал за {count} попыток.')
            break
    else:
        print('Не угадал! Попытки исчерпаны.')


if __name__ == '__main__':
    pass
