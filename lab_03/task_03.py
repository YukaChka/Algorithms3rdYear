n = int(input("Число N: "))

# Сумма нечётных растёт квадратами: 1, 4, 9, 16 и дальше.
total = 0
for i in range(1, n + 1):
    total += 2 * i - 1
    print("Текущая сумма:", total)
