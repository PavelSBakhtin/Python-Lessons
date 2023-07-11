# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой.

from decimal import *
import math

d = input("Enter diameter: ")
getcontext().prec = 42
decimal_dia = Decimal(d)

if 0 < float(d) <= 1000:
    area = Decimal(math.pi) * (decimal_dia / 2) ** 2
    circumference = Decimal(math.pi) * decimal_dia

    print("ДЛИНА ОКРУЖНОСТИ = ", circumference)
    print("ПЛОЩАДЬ КРУГА = ", area)
else:
    print("Диаметр больше 1000 у.е.")
