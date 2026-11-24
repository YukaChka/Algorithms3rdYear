from math import prod

# K — номер строки для человека, поэтому индекс в списке на единицу меньше.
m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

k = int(input("Номер строки K: "))
row = matrix[k - 1]
print("Сумма:", sum(row))
print("Произведение:", prod(row))
