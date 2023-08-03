# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, sample, shuffle

name_list = []


def generate_aliases(lists):
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщъь'
    name_counts = int(input('Number of aliases to generate: '))
    for _ in range(0, name_counts):
        name_length = randint(4, 7)
        count_vowels = randint(1, name_length - 2)
        count_consonants = name_length - count_vowels
        name_vowels = sample(vowels, count_vowels)
        name_consonants = sample(consonants, count_consonants)
        aliase = name_vowels + name_consonants
        shuffle(aliase)
        final_aliase = ''.join(aliase).title()
        lists.append(final_aliase)
    return lists


def file_entry():
    data = generate_aliases(name_list)
    with open('lesson7_task2.txt', 'a', encoding='utf-8') as f:
        for line in data:
            print(line, end='\n', file=f)


file_entry()
print(*name_list)
