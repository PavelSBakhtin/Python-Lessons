# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления;
# Избегайте магических чисел;
# Добавьте аннотацию типов где это возможно.

def decimal_to_binary(num: int) -> str:
    binary = ""
    if num == 0:
        binary = "0"
    else:
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
    return binary

def decimal_to_octal(num: int) -> str:
    binary = ""
    if num == 0:
        binary = "0"
    else:
        while num > 0:
            binary = str(num % 8) + binary
            num = num // 8
    return binary

number = int(input("Enter a number\n"))
print(decimal_to_binary(number), end=" - ")
print(bin(number))
print(decimal_to_octal(number), end=" - ")
print(oct(number))
