# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

def call_count(num):
    def decorator(func):
        result = []
        # если в for вариант №2, то - # result = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result.append(func(*args, **kwargs))
                # result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@call_count(5)
def printer(string):
    print(string)
    return 'ok'


print(printer('сработало!'))


# # ещё пример:

# def counter(func):
#     def wrapper(count):
#         for i in range(count):
#             func()
#     return wrapper

# @counter
# def printer():
#     print("data")

# printer(5)
