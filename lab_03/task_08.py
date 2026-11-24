n = int(input("Число N: "))

# Условие проверяем по сумме. Она может перескочить через N, и это нормально.
k = 0
total = 0
while total < n:
    k += 1
    total += k

print("Наименьшее K:", k)
print("Сумма:", total)
