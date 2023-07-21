# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# Вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# * Превратите решение в генераторное выражение.

lst = (i for i in range(1, 101))
for i in lst:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print(*('FizzBuzz' if not i % 15 else "Buzz" if not i % 5 else "Fizz" if not i % 3 else i for i in range(1, 101)))
