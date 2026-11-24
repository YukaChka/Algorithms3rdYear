def hanoi(n, source, target, spare):
    if n < 0:
        raise ValueError("Количество дисков должно быть неотрицательным.")
    if n == 0:
        return

    hanoi(n - 1, source, spare, target)
    print(f"Диск {n}: {source} → {target}")
    hanoi(n - 1, spare, target, source)


# Чтобы перенести большой диск, сначала надо освободить его от всех маленьких.
if __name__ == "__main__":
    n = int(input("Количество дисков: "))
    hanoi(n, "A", "C", "B")
