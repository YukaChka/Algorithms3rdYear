n = int(input("Количество сомножителей N: "))

# Номер шага определяет добавку к единице: на третьем шаге множитель 1.3.
product = 1.0
for i in range(1, n + 1):
    factor = 1 + i / 10
    product *= factor

print("Произведение:", product)
