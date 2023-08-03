# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# - если результат умножения отрицательный,
# сохраните имя записанное строчными буквами и произведение по модулю;
# - если результат умножения положительный,
# сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.

from itertools import cycle


def write_file():
    f1_size = len(list(1 for _ in open('lesson7_task1.txt')))
    f2_size = len(list(1 for _ in open('lesson7_task2.txt')))
    count = max(f1_size, f2_size)

    with open('lesson7_task1.txt', 'r', encoding='utf-8') as f1, \
        open('lesson7_task2.txt', 'r', encoding='utf-8') as f2, \
            open('lesson7_task3.txt', 'w', encoding='utf-8') as f3:
        f1_list = cycle(f1.readlines())
        f2_list = cycle(f2.readlines())
        for _ in range(count):
            f1_item_1, f1_item_2 = next(f1_list).split('|')
            f1_res = round(float(f1_item_1) * float(f1_item_2), 3)
            if f1_res < 0:
                print(f'{next(f2_list).strip().lower()}:{abs(f1_res)}', file=f3)
            else:
                print(f'{next(f2_list).strip().upper()}:{round(f1_res)}', file=f3)


write_file()
