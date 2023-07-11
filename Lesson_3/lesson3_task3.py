# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

from pprint import pprint

my_tuple = (True, "String", 2, False, 5.16, 4-3j, [1, 4, 5], (3, 4, 6), {2, 5, 5, 7, 6}, {4, 7, 6}, 43, 'second')

result_dict = {}

for i in my_tuple:
    if type(i).__name__ not in result_dict:
        result_dict[type(i).__name__] = []
    result_dict[type(i).__name__].append(i)

pprint(result_dict)
