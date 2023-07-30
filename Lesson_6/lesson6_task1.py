# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные
# в модуль функции под псевдонимами. (3-7 строк импорта).

# Примеры использования импортов:

import random as rnd

a = rnd.randint(0, 10)
print(a)

from random import randint as rnd_int

b = rnd_int(0, 10)
print(b)

from sys import * # всё из модуля, не рекомендуется так
import os 
