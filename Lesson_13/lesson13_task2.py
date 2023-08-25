# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

my_dict = {'1': 2, '2': 4}


def dict_get(inp_dict: dict, key=None, value=None):
    try:
        return inp_dict[key]
    except:
        return value


print(my_dict)
print(dict_get(my_dict, '1'))
print(dict_get(my_dict, '3', 5))
