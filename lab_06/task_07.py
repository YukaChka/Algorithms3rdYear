m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# Сначала ищем столбцы во всей матрице, потом выполняем обмен во всех строках.
minimum = maximum = matrix[0][0]
min_col = max_col = 0
for row in matrix:
    for col, value in enumerate(row):
        if value < minimum:
            minimum, min_col = value, col
        if value > maximum:
            maximum, max_col = value, col

for row in matrix:
    row[min_col], row[max_col] = row[max_col], row[min_col]
    print(*row)
