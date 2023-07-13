# Напишите программу банкомат:
# Начальная сумма равна нулю;
# Допустимые действия: пополнить, снять, выйти;
# Сумма пополнения и снятия кратны 50 у.е.;
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.;
# После каждой третей операции пополнения или снятия начисляются проценты - 3%;
# Нельзя снять больше, чем на счёте;
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной;
# Любое действие выводит сумму денег.

balance = 0
count = 0
ACTION = 50
COMMISSION = 0.015
BONUS = 1.03
TAX = 1.10
MIN_FEE = 30
MAX_FEE = 600

while True:
    print("========== БАНКОМАТ ==========")
    print("1. ПОПОЛНИТЬ")
    print("2. СНЯТЬ")
    print("3. ВЫЙТИ")
    match int(input("ВЫБЕРИТЕ ДЕЙСТВИЕ:\n ->")):
        case 1:
            dep = int(input("ВВЕДИТЕ СУММУ ПОПОЛНЕНИЯ: "))
            if dep % 50 == 0:
                if count % 3 == 0:
                    balance += dep
                    balance *= BONUS
                    count += 1
                    print(f"БАЛАНС СОСТОВЛЯЕТ: {balance} у.е.")
                else:
                    balance += dep
                    count += 1
                    print(f"БАЛАНС СОСТОВЛЯЕТ: {balance} у.е.")
            else:
                print("ПОПОЛНЕНИЕ ТОЛЬКО КРАТНО 50 у.е.")
        case 2:
            withdraw = int(input("CУММА CНЯТИЯ: "))
            if withdraw % 50 == 0 and withdraw < balance:
                fee = withdraw * COMMISSION
                if MIN_FEE < fee < MAX_FEE:
                    if count % 3 == 0:
                        balance -= withdraw - fee
                        balance *= BONUS
                        count += 1
                        print(f"БАЛАНС СОСТОВЛЯЕТ: {balance} у.е.")
                    else:
                        balance -= withdraw - fee
                        count += 1
                        print(f"БАЛАНС СОСТОВЛЯЕТ: {balance} у.е.")
            else:
                print("СУММА СНЯТИЯ ПРЕВЫШАЕТ БАЛАНС СЧЕТА!")
        case 3:
            exit()
