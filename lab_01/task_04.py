a = float(input("Первое ненулевое число: "))
b = float(input("Второе ненулевое число: "))

# Квадраты пригодятся четыре раза. Посчитаем каждый один раз.
a_squared = a ** 2
b_squared = b ** 2

print("Сумма квадратов:", a_squared + b_squared)
print("Разность квадратов:", a_squared - b_squared)
print("Произведение квадратов:", a_squared * b_squared)
print("Частное квадратов:", a_squared / b_squared)
