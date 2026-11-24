m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# В каждой строке свой минимум и максимум, значит и обмен свой.
for row in matrix:
    min_col = row.index(min(row))
    max_col = row.index(max(row))
    row[min_col], row[max_col] = row[max_col], row[min_col]
    print(*row)
