# Работа в консоли в режиме интерпретатора Python.
# Решите квадратное уравнение 5x^2-10x-400=0 последовательно, сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print('{}x^2 + {}x + {} = 0'.format(a, b, c))
if a == 0:
    if b == 0:
        if c == 0:
            print('the equation has an infinite number of roots')
        else:
            print('equation writing error')
    else:
        print('linear equation {}x + {} = 0'.format(b, c))
        x1 = -c / b
        print('there is only one root in the equation: x1 = ', x1)
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print('there are no real roots in the equation')
    elif discriminant == 0:
        x1 = -b / (2 * a)
        print('there is only one root in the equation: x1 = ', x1)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('first root of the equation x1 = ', x1)
        print('second root of the equation x2 = ', x2)
