m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# У соответствующих ячеек двух четвертей одинаковая позиция внутри своей четверти.
half_m = m // 2
half_n = n // 2

for row in range(half_m):
    for col in range(half_n):
        lower_row = row + half_m
        right_col = col + half_n
        matrix[row][col], matrix[lower_row][right_col] = (
            matrix[lower_row][right_col], matrix[row][col]
        )

for row in matrix:
    print(*row)
