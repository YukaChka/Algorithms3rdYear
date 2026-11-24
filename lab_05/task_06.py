numbers = list(map(float, input("Элементы массива через пробел: ").split()))
k = int(input("Номер первого элемента K: "))
l = int(input("Номер последнего элемента L: "))

# K переводим в индекс с нуля. Правая граница среза уже исключается.
selected = numbers[k - 1:l]
average = sum(selected) / len(selected)

print("Среднее арифметическое:", average)
