# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    for j in range(2, 6):
        print(f'{j} X {i} = {i * j}', end='\t\t')
    print()
print()
for i in range(2, 11):
    for j in range(6, 10):
        print(f'{j} X {i} = {i * j}', end='\t\t')
    print()
