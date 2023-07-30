# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__days_dict = {31: (1, 3, 5, 7, 8, 10, 12), 30: (4, 6, 9, 11)}
__feb_norm = 28
__feb_leap = 29


def _check_year(year):
    if (year % 4 != 0 or year % 100 == 0 and year % 400 != 0):
        result = 'Normal year'
    else:
        result = 'Leap-year'
    return result


def check_date(date):
    day, month, year = map(int, date.split('.'))
    if 0 < year < 10000 and 0 < month < 13 and 0 < day < 32:
        if day in __days_dict.keys() and month in __days_dict[day] or month != 2 and day < 30:
            return True
        if month == 2 and day < 30:
            if _check_year(year) == 'Normal year':
                return day <= __feb_norm
            if _check_year(year) == 'Leap-year':
                return day <= __feb_leap
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    pass
