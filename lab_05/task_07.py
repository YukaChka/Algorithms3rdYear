numbers = list(map(int, input("Различные целые числа через пробел: ").split()))

# Разность первой пары служит образцом для всех остальных пар соседей.
difference = 0
if len(numbers) >= 2:
    difference = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i - 1] != difference:
            difference = 0
            break

print(difference)
