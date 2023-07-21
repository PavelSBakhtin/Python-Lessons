# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def simple_generator(n):
    count = 0
    current = 2
    while count < n:
        flag = True
        for i in range(2, current // 2 + 1):
            if not current % i:
                flag = False
        current += 1
        if flag:
            count += 1
            yield current - 1


generator = simple_generator(int(input('Введите N: ')))

print(*generator)
