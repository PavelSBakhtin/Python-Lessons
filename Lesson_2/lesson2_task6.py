# Напишите программу банкомат:
# Начальная сумма равна нулю;
# Допустимые действия: пополнить, снять, выйти;
# Сумма пополнения и снятия кратны 50 у.е.;
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.;
# После каждой третей операции пополнения или снятия начисляются проценты - 3%;
# Нельзя снять больше, чем на счёте;
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной;
# Любое действие выводит сумму денег.

balance = 0 # баланс
count = 0 # счётчик пополнени/снияти
ACTION = 50 # кратность
COMMISSION = 0.015 # % за снятие
MIN_FEE = 30 # минимум такса при снятии
MAX_FEE = 600 # максимум такса при снятии
BONUS = 1.03 # % на остаток
LIMIT = 5000000 # порог богатства
TAX = 0.10 # налог на богатство

while True:
    print('\n========== БАНКОМАТ ==========')
    if balance > LIMIT:
        balance -= (balance * TAX)
    print(f'Баланс: {balance} у.е.')
    print('1. ПОПОЛНИТЬ')
    print('2. СНЯТЬ')
    print('3. ВЫЙТИ')
    menu = int(input('Выберите пункт меню: '))
    if menu == 1:
        print('\nПополнение баланса >>>')
        depo_plus = int(input('Введите сумму пополнения: '))
        if depo_plus % ACTION == 0:
            count += 1
            balance += depo_plus
        else:
            print('\nПополнение невозможно, только кратно 50 у.е.')
        print(f'\nБаланс пополнен на сумму: {depo_plus}')
        if count % 3 == 0:
            balance *= BONUS
            round(balance, 2)
            print('\nВам начислено 3% на остаток')
        print(f'\nБаланс: {balance} у.е.')
    elif menu == 2:
        print('\nСниятие с баланса >>>')
        depo_minus = int(input('Введите сумму снятия: '))
        if depo_minus % ACTION == 0:
            fee = round(depo_minus * COMMISSION, 2)
            if fee < MIN_FEE:
                fee = MIN_FEE
            elif fee > MAX_FEE:
                fee = MAX_FEE
            total = depo_minus + fee
            if total < balance:
                count += 1
                balance -= total
            else:
                print('\nНедостаточно средств')
        else:
            print('\nСнятие невозможно, только кратно 50 у.е.')
        print(f'\nБаланс уменьшен на сумму: {total}')
        if count % 3 == 0:
            balance *= BONUS
            round(balance, 2)
            print('\nВам начислено 3% на остаток')
        print(f'\nБаланс: {balance} у.е.')
    elif menu == 3:
        print(f'\nБаланс: {balance} у.е.')
        exit()
    else:
        print(f'\nБаланс: {balance} у.е.')
        print(f'\nНеверно введена команда')
