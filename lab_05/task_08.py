numbers = list(map(float, input("Элементы массива через пробел: ").split()))

# Второй элемент сидит по индексу 1. Оттуда берём каждый второй.
even_positions = numbers[1::2]
if even_positions:
    print("Минимум:", min(even_positions))
else:
    print("В массиве нет элементов с чётными номерами.")
