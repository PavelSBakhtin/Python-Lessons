# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата: Сколько рядов у ёлки? - 5
#
#     *
#    ***
#   *****
#  *******
# *********

n = int(input('How many rows does the tree have? '))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
