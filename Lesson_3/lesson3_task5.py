# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

print(my_list := [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9])

print(*[i+1 for i in range(len(my_list)) if my_list[i] % 2])

# my_list = [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9]

# result = []

# for i in range(len(my_list)):
#     if my_list[i] % 2:
#         result.append(i+1)

# print(*result)
