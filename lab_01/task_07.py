a = float(input("Координата A: "))
b = float(input("Координата B: "))
c = float(input("Координата C: "))

# Вычитание даёт направление, модуль оставляет только длину.
ac = abs(c - a)
bc = abs(c - b)

print("Длина AC:", ac)
print("Длина BC:", bc)
print("Сумма длин:", ac + bc)
