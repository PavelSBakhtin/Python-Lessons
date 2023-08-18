# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# - возврат строки без изменений;
# - возврат строки с преобразованием регистра без потери символов;
# - возврат строки с удалением знаков пунктуации;
# - возврат строки с удалением букв других алфавитов;
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1).

import pytest
from lesson14_task2 import removal


def test_ret_same():
    assert (removal('language') == 'language')


def test_lower():
    assert (removal('LanguagE') == 'language')


def test_punt():
    assert (removal('l,an.gu:a!g?e') == 'language')


def test_non_rus():
    assert (removal('lфanguage') == 'language')


def test_non_all():
    assert (removal('Lфв,an.gu:a!g?E') == 'language')


if __name__ == '__main__':
    pytest.main(['-v'])
