from math import hypot

# Сравниваем два расстояния от одной и той же точки A.
ax = float(input("x точки A: "))
ay = float(input("y точки A: "))
bx = float(input("x точки B: "))
by = float(input("y точки B: "))
cx = float(input("x точки C: "))
cy = float(input("y точки C: "))

ab = hypot(bx - ax, by - ay)
ac = hypot(cx - ax, cy - ay)

if ab < ac:
    print(f"Ближе точка B ({bx}, {by}). Расстояние: {ab}")
elif ac < ab:
    print(f"Ближе точка C ({cx}, {cy}). Расстояние: {ac}")
else:
    print(f"Точки B и C равноудалены от A. Расстояние: {ab}")
