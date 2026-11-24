from decimal import Decimal

# Считаем десятые доли целыми шагами. Последний шаг даёт ровно килограмм.
price = Decimal(input("Цена 1 кг конфет: "))

for tenths in range(1, 11):
    weight = Decimal(tenths) / 10
    print(f"{weight:.1f} кг — {price * weight} руб.")
