from decimal import Decimal

# Отрезки вычитаем по одному, пока очередной ещё помещается.
a = Decimal(input("Длина отрезка A: "))
b = Decimal(input("Длина отрезка B: "))

remaining = a
while remaining >= b:
    remaining -= b

print("Длина незанятой части:", remaining)
