x = float(input("x: "))
y = float(input("y: "))

# Знаки x и y вместе определяют четверть. Ноль означает попадание на ось.
if x == 0 or y == 0:
    print("Точка лежит на оси координат.")
elif x > 0 and y > 0:
    print("Четверть: 1")
elif x < 0 and y > 0:
    print("Четверть: 2")
elif x < 0 and y < 0:
    print("Четверть: 3")
else:
    print("Четверть: 4")
