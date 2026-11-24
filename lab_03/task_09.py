from decimal import Decimal

# Процент начисляется на текущий вклад. Ровно 1100 ещё не повод остановиться.
percent = Decimal(input("Процент начисления за месяц P: "))
monthly_rate = percent / 100

balance = Decimal(1000)
months = 0
while balance <= 1100:
    balance += balance * monthly_rate
    months += 1

print("Количество месяцев:", months)
print("Итоговый размер вклада:", balance)
