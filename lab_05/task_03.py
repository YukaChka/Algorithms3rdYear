n = int(input("Размер массива N: "))
a = int(input("Первый элемент A: "))
b = int(input("Второй элемент B: "))

# После добавления очередной суммы накопленная сумма удваивается.
numbers = [a, b]
total = a + b
for _ in range(2, n):
    numbers.append(total)
    total += numbers[-1]

print(*numbers)
