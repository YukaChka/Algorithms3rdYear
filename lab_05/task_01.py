n = int(input("Размер массива N: "))

# У нечётных чисел шаг 2, а первое число получается при i = 0.
numbers = []
for i in range(n):
    numbers.append(2 * i + 1)

print(*numbers)
