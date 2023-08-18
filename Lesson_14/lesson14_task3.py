# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# - возврат строки без изменений;
# - возврат строки с преобразованием регистра без потери символов;
# - возврат строки с удалением знаков пунктуации;
# - возврат строки с удалением букв других алфавитов;
# - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1).

import unittest
from lesson14_task2 import removal


class TestRemoval(unittest.TestCase):
    
    def test_ret_same(self):
        self.assertEqual(removal('language'), 'language')

    def test_lower(self):
        self.assertEqual(removal('LanguagE'), 'language')

    def test_punt(self):
        self.assertEqual(removal('l,an.gu:a!g?e'), 'language')

    def test_non_rus(self):
        self.assertEqual(removal('lфanguage'), 'language')

    def test_non_all(self):
        self.assertEqual(removal('Lфв,an.gu:a!g?E'), 'language')


unittest.main(verbosity=2)
