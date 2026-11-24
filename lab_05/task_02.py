n = int(input("Размер массива N: "))
a = float(input("Первый член A: "))
d = float(input("Знаменатель D: "))

# Каждый следующий член проще получить из последнего, уже записанного в список.
numbers = [a]
for _ in range(1, n):
    numbers.append(numbers[-1] * d)

print(*numbers)
