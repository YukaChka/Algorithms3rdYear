a = int(input("A: "))
b = int(input("B: "))

# Если числа одинаковые, победителя нет: обоим достаётся ноль.
if a > b:
    b = a
elif b > a:
    a = b
else:
    a = b = 0

print("Новые значения A и B:", a, b)
