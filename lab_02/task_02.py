a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

# Чтобы сложить два наибольших, достаточно выяснить, кого оставить за бортом.
if a <= b and a <= c:
    result = b + c
elif b <= a and b <= c:
    result = a + c
else:
    result = a + b

print("Сумма двух наибольших чисел:", result)
