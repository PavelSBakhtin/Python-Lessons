# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9]

i = 0
while i < len(my_list):
    if my_list.count(my_list[i]) == 2:
        temp = my_list[i]
        my_list.remove(temp) 
        my_list.remove(temp)
    else:
        i += 1

print(my_list)
