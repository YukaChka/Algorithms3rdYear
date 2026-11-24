numbers = list(map(float, input("Элементы массива через пробел: ").split()))

# У первого элемента номер 1, а индекс 0. Поэтому берём срез с нулевого индекса.
odd_positions = numbers[::2]
even_positions = numbers[1::2]

print(*odd_positions, *reversed(even_positions))
