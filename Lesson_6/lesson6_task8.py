# Создайте пакет со всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции,
# которые могут верно работать за пределами модуля.

from lesson6_modules import guess_num, quest, check_date


def menu_selection(menu):
    if menu == 2:
        guess_num(1, 10, 5)  # task 2
    elif menu == 4:
        quest('Сколько ног у муравья?', ['1', '2', '3', '4', '5', '6'], 3)  # task 4
    elif menu == 7:
        print(check_date(input('Enter a date in the format DD.MM.YYYY - ')))  # task 7
    else:
        print('Wrong choice')


menu_selection(int(input('Choose a task (2, 4, 7): ')))
