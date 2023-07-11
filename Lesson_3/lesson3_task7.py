# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

from collections import Counter

obj = input('Введите строку >>> ')

result1 = {}
result2 = {}
result3 = Counter(obj)
result4 = {}

for i in obj:
    result1[i] = result1.setdefault(i, 0) + 1

for i in obj:
    if i not in result2:
        result2[i] = obj.count(i)

for i in obj:
    if i not in result4:
        result4[i] = 0
    result4[i] += 1

print(result1, result2, result4, result3, sep = '\n')
