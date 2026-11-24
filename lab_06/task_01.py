m = int(input("Порядок матрицы M: "))
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != m:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# Начинаем спускаться по левому краю. После каждого участка сдвигаем границу.
result = []
top, bottom = 0, m - 1
left, right = 0, m - 1

while top <= bottom and left <= right:
    for row in range(top, bottom + 1):
        result.append(matrix[row][left])
    left += 1
    for col in range(left, right + 1):
        result.append(matrix[bottom][col])
    bottom -= 1
    if left <= right:
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][right])
        right -= 1
    if top <= bottom:
        for col in range(right, left - 1, -1):
            result.append(matrix[top][col])
        top += 1

print(*result)
