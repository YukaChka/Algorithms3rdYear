x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# От порядка ввода вершин ширина и высота зависеть не должны.
width = abs(x2 - x1)
height = abs(y2 - y1)

print("Периметр:", 2 * (width + height))
print("Площадь:", width * height)
