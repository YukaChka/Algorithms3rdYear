def fibonacci(n):
    if n < 0:
        raise ValueError("Номер числа должен быть неотрицательным.")

    def advance(steps, current, following):
        if steps == 0:
            return current
        return advance(steps - 1, following, current + following)

    return advance(n, 0, 1)


# Для следующего шага достаточно помнить два соседних числа Фибоначчи.
if __name__ == "__main__":
    n = int(input("Номер числа n (F(0) = 0, F(1) = 1): "))
    print("Число Фибоначчи:", fibonacci(n))
