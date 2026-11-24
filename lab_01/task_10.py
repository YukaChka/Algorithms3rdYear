from math import hypot

# Периметру нужны три стороны, а для площади хватит двух векторов из одной вершины.
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

ab = hypot(x2 - x1, y2 - y1)
bc = hypot(x3 - x2, y3 - y2)
ca = hypot(x1 - x3, y1 - y3)

# Половина модуля определителя двух векторов из первой вершины.
area = abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) / 2

print("Периметр:", ab + bc + ca)
print("Площадь:", area)
