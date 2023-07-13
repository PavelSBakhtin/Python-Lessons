# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга?
# Какие вещи уникальны, есть только у одного друга?
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

# Например: Иванов, Петров, Сидоров
# 1й взял: нож, котел, спички, палатка
# 2й взял: топор, вода, спички, вилка
# 3й взял: топор, вода, спички, вилка

friends = input('Введите друзей, отправившихся в подох (через запятую): ').split(', ')
things = {}
i = 0
for friend in friends:
    things.setdefault(friend, tuple(input(f'{friends[i]} взял с собой (через запятую): ').split(', ')))

res = []
for th in things.values():
    for j in th:
        res.append(j)

only = []
for k in res:
    if k not in only:
        only.append(k)
print('Все друзья взяли с собой:', *only)

uniq = []
n = 0
while n < len(res):
    uniq.append(res[n])
    n += 1
n = 0
while n < len(uniq):
    if uniq.count(uniq[n]) > 1:
        h = uniq.count(uniq[n])
        temp = uniq[n]
        while h > 0:
            uniq.remove(temp)
            h -= 1
    else:
        n += 1
print('Уникальные вещи, есть только у одного из друзей: ', *uniq)

many = []
x = 0
while x < len(res):
    many.append(res[x])
    x += 1
x = 0
while x < len(many):
    if many.count(many[x]) == 1:
        many.remove(many[x])
    else:
        x += 1
x = 0
while x < len(many):
    if many.count(many[x]) == len(things):
        h = many.count(many[x])
        temp = many[x]
        while h > 0:
            many.remove(temp)
            h -= 1
    else:
        x += 1
x = 0
while x < len(many):
    if many.count(many[x]) > 1:
        many.remove(many[x])
    else:
        x += 1
print(friends)
for s in many:
    for t in friends:
        if s in things[t]:
            friends.remove(t)
print('Эти вещи есть у всех друзей: ', *many, '; кроме ', *friends)
