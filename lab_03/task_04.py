a = float(input("Число A: "))
n = int(input("Степень N: "))

# Для следующей степени достаточно ещё раз умножить предыдущую на A.
total = 1.0
term = 1.0
for _ in range(n):
    term *= a
    total += term

print("Сумма:", total)
