def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


# Каждый рекурсивный шаг отдаёт одно простое слагаемое и уменьшает остаток.
def prime_sum(n):
    if n < 2:
        raise ValueError("Для разложения нужно целое число не меньше 2.")
    if is_prime(n):
        return [n]

    # Остаток должен быть не меньше 2, чтобы его тоже можно было разложить.
    prime = n - 2
    while not is_prime(prime):
        prime -= 1

    return [prime] + prime_sum(n - prime)


if __name__ == "__main__":
    n = int(input("Целое число не меньше 2: "))
    terms = prime_sum(n)
    print(f"{n} = " + " + ".join(map(str, terms)))
