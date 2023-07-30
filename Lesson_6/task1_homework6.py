# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from lesson6_modules import check_date
from sys import argv

# Вариант передачи даты напрямую:
print(check_date(argv[1]))

# # Вариант без передачи даты напрямую:
# print(check_date(input('Enter a date in the format DD.MM.YYYY - ')))

# В консоле:
# cd Lesson_6/
# python task1_homework6.py 29.02.2001
# cd ..
