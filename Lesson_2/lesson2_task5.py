# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

import cmath

a = float(input('Enter a: ')) 
b = float(input('Enter b: ')) 
c = float(input('Enter c: ')) 
 
# calculate the discriminant 
d =(b**2) -(4*a*c) 
 
# find two solutions 
sol1 =(-b-cmath.sqrt(d))/(2*a) 
sol2 =(-b+cmath.sqrt(d))/(2*a) 
print('The solutions are {0} and {1}'.format(sol1,sol2))

# другие решения:
# a, b, c = map(float, input("Enter the kof\n -> ").split())
# d = (b ** 2) - (4 * a * c)
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
# print(f'\n{sol1}\n{sol2}')


# print("решаем квадратное уравнение ax^2+bx+c = 0")
# a =float(input("a"))
# print("вы ввели a=", a)
# b = float(input("b"))
# print("вы ввели b= ", b)
# c = float(input("c"))
# print("вы ввели c=", c)

# print("решаем квадратное уравнение {}x^2 + {}x + {} = 0".format (a,b,c))
# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("уравнений имеет бесконечное число корней")
#         else:
#             print("ошибка записи уравнения")
#     else:
#         print("уравнение линейного вида {}x+{} = 0".format(b,c))
#         x1 = -c / b
#         print("у уравнения только один корень x1= ", x1)
# else:
#     discriminant = b**2-4*a*c
#     if discriminant < 0:
#         print("у уравнения нет вещественных корней")
#     elif discriminant == 0:
#         x1 = -b / (2 * a)
#         print("у уравнения только один корень x1= ", x1)
#     else:
#         x1 = (-b + discriminant**0.5) / (2 * a)
#         x2 = (-b - discriminant**0.5) / (2 * a)
#         print("первый корень уравнения x1= ", x1)
#         print("второй корень уравнения x2= ", x2)
