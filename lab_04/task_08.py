def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


# Деление нацело на 10 убирает последнюю цифру. Знак в счёт не идёт.
if __name__ == "__main__":
    n = int(input("Целое число: "))
    print("Количество цифр:", count_digits(n))
