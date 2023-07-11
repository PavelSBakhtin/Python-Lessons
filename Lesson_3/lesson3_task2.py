# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# - Целое положительное число;
# - Вещественное положительное или отрицательное число;
# - Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква;
# - Строку в верхнем регистре в остальных случаях.

s = input('Enter string: ')
if s.isdigit():
    print('positive integer: ', int(s))
else:
    try:
        print('float number: ', float(s))
    except:
        if any(i.isupper() for i in s):
            print('there is a capital letter in the string: ', s.lower())
        else:
            print('to lower case', s.upper())
