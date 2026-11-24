# Ищем справа налево, чтобы первый найденный максимум оказался последним в массиве.
numbers = list(map(float, input("Элементы массива через пробел: ").split()))

# Крайний элемент сравнивается с единственным соседом.
for i in range(len(numbers) - 1, -1, -1):
    greater_than_left = i == 0 or numbers[i] > numbers[i - 1]
    greater_than_right = i == len(numbers) - 1 or numbers[i] > numbers[i + 1]
    if greater_than_left and greater_than_right:
        print("Номер последнего локального максимума:", i + 1)
        break
else:
    print("Локальных максимумов нет.")
