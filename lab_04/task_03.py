def power(x, n):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1

    half = power(x, n // 2)
    squared = half * half
    if n % 2 == 0:
        return squared
    return x * squared


# Одну половину степени вычисляем один раз и используем дважды.
if __name__ == "__main__":
    x = float(input("Основание x: "))
    n = int(input("Целая степень n: "))
    print("Результат:", power(x, n))
