def binary_search(numbers, target):
    def search(left, right):
        if left > right:
            return -1

        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            return search(middle + 1, right)
        return search(left, middle - 1)

    return search(0, len(numbers) - 1)


# Границы поиска сдвигаются, сам список остаётся на месте.
if __name__ == "__main__":
    numbers = list(map(int, input("Отсортированные целые числа через пробел: ").split()))
    target = int(input("Искомое число: "))
    index = binary_search(numbers, target)
    if index == -1:
        print("Элемент не найден.")
    else:
        print("Индекс элемента (с нуля):", index)
