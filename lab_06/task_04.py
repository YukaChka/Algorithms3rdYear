m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(float, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# У каждого столбца своё среднее. Значения ровно на среднем не считаются.
for number, column in enumerate(zip(*matrix), start=1):
    average = sum(column) / m
    count = sum(value > average for value in column)
    print(f"Столбец {number}: {count}")
