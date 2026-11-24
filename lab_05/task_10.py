numbers = list(map(int, input("Целые числа через пробел: ").split()))

# Запоминаем номер при первом появлении числа, при повторе оба номера уже известны.
positions = {}
for position, number in enumerate(numbers, start=1):
    if number in positions:
        print(positions[number], position)
        break
    positions[number] = position
