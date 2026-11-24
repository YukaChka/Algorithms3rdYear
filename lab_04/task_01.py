def factorial(n):
    if n < 0:
        raise ValueError("Факториал определён для неотрицательных целых чисел.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Доходим до 1 или 0, а умножения собираются на обратном пути.
if __name__ == "__main__":
    n = int(input("Неотрицательное целое число n: "))
    print("Факториал:", factorial(n))
