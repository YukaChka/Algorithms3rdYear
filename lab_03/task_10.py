a = int(input("Число A: "))
b = int(input("Число B: "))

# Каждый шаг Евклида заменяет пару чисел делителем и остатком.
while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("НОД:", a)
