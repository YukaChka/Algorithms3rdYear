a = float(input("Число A: "))
n = int(input("Степень N: "))

# Умножение на −A сразу меняет знак и увеличивает степень.
total = 1.0
term = 1.0
for _ in range(n):
    term *= -a
    total += term

print("Сумма:", total)
