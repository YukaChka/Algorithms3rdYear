m, n = map(int, input("Число строк M и столбцов N через пробел: ").split())
print("Введите строки матрицы, разделяя элементы пробелами:")
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError("Неверное количество элементов в строке.")
    matrix.append(row)

# Как только нашёлся подходящий столбец, дальше смотреть незачем.
for number, column in enumerate(zip(*matrix), start=1):
    if all(value % 2 != 0 for value in column):
        print(number)
        break
else:
    print(0)
