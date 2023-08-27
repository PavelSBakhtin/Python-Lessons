# Создайте класс с базовым исключением и дочерние классы-исключения:
# - ошибка уровня,
# - ошибка доступа.


class UserException(Exception):
    pass


class UserLevelError(UserException):
    pass


class UserPermissionError(UserException):
    pass


raise UserLevelError('текст ошибки')
