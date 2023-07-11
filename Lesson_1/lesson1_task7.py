# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено:
# цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25.
# Для двузначного числа произведение цифр, например 30 - 0.
# Для трёхзначного числа его зеркальное отображение, например 520 - 25.
# Если число не из диапазона, запросите новое число.
# Откажитесь от магических чисел.
# В коде должны быть один input и один print.

while True:
    n = int(input('Enter number from 1 to 999: '))
    if n < 1 or n > 999:
        continue
    if 10 > n > 0:
        res = f"A number is entered, its square = {n ** 2}"
    elif 9 < n < 100:
        res = f"Two-digit number entered, product of digits = {(n // 10) * (n % 10)}"
    else:
        res = f"A three-digit number is entered, its mirror = {int(str(n)[::-1])}"
    print(res)
    break
