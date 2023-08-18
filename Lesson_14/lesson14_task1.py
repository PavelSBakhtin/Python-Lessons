# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters


def removal(input_str):

    rezult = ''
    for i in input_str:
        if i in ascii_letters or i == ' ':
            rezult += i.lower()
    return rezult


input_str = 'Pф3$y.t,hoN| i**s --a g(o)Od LanguagE'
print(f'Исходная строка: {input_str}')
print(removal(input_str))


# def string_cleaner(s):
    # return re.sub(r'[^a-z ]*', '', s.lower())
