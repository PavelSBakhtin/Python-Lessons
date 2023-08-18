# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# - возврат строки без изменений;
# - возврат строки с преобразованием регистра без потери символов;
# - возврат строки с удалением знаков пунктуации;
# - возврат строки с удалением букв других алфавитов;
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1).

from string import ascii_letters
from doctest import testmod


def removal(input_str):
    """
    Удаляет все символы, кроме латинских букв в нижнем регистре и пробелов:
    >>> removal('language')
    'language'
    >>> removal('LanguagE')
    'language'
    >>> removal('l,an.gu:a!g?e')
    'language'
    >>> removal('lфanguage')
    'language'
    >>> removal('Lфв,an.gu:a!g?E')
    'language'
    """
    rezult = ''
    for i in input_str:
        if i in ascii_letters or i == ' ':
            rezult += i.lower()
    return rezult


# input_str = 'Pф3$y.t,hoN| i**s --a g(o)Od LanguagE'
# print(f'Исходная строка: {input_str}')
# print(removal(input_str))

testmod(verbose=True)
