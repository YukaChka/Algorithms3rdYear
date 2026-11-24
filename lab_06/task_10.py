# У элементов одной диагонали разность индексов столбца и строки постоянна.
m = int(input("Порядок матрицы M: "))
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != m:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# Перебираем диагонали от нижнего левого угла до верхнего правого.
for offset in range(1 - m, m):
    start_row = max(0, -offset)
    end_row = min(m, m - offset)
    total = sum(matrix[row][row + offset] for row in range(start_row, end_row))
    print(total)
