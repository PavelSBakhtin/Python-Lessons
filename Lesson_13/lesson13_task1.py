# # Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def input_float():
    try:
        return float(input('Enter float number -> '))
    except ValueError:
        print('Invalid value, expected float number through dot("."): ')
        return input_float()


def get_num():
    while True:
        try:
            num = float(input('Введите число: '))
            if num.is_integer(): # >>> if num - int(num) == 0:
                num = int(num)
            break
        except ValueError:
            print('Ошибка ввода!')
    return num


# print(input_float())
print(get_num())
