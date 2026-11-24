from math import prod

# При равных произведениях сохраняем столбец, который встретился первым.
m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

best_column = 1
best_product = prod(row[0] for row in matrix)
for col in range(1, n):
    product = prod(row[col] for row in matrix)
    if product < best_product:
        best_column = col + 1
        best_product = product

print("Номер столбца:", best_column)
print("Наименьшее произведение:", best_product)
