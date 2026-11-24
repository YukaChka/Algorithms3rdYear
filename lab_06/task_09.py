m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# Первые элементы служат ключами сортировки, а переезжают строки целиком.
matrix.sort(key=lambda row: row[0])

for row in matrix:
    print(*row)
