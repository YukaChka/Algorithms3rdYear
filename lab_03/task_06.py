a = int(input("Начало диапазона A: "))
b = int(input("Конец диапазона B: "))

# Внешний цикл выбирает число, внутренний отвечает за количество копий.
for number in range(a, b + 1):
    for _ in range(number):
        print(number)
