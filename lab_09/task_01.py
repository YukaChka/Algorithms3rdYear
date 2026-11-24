from decimal import Decimal


def selection_sort(numbers):
    """Сортирует список на месте и возвращает число сравнений и обменов."""
    comparisons = 0
    swaps = 0

    for start in range(len(numbers) - 1):
        # Даже когда обменов ноль, минимум среди оставшихся всё равно надо проверить.
        min_index = start
        for index in range(start + 1, len(numbers)):
            comparisons += 1
            if numbers[index] < numbers[min_index]:
                min_index = index

        if min_index != start:
            numbers[start], numbers[min_index] = numbers[min_index], numbers[start]
            swaps += 1

    return comparisons, swaps


if __name__ == "__main__":
    line = input("Введите числа через пробел (Enter — сравнить два массива): ")

    if line.strip():
        examples = [list(map(Decimal, line.split()))]
    else:
        examples = [[1, 2, 3, 4, 5], [5, 1, 2, 3, 4]]

    for numbers in examples:
        print("Исходный массив:", *numbers)
        comparisons, swaps = selection_sort(numbers)
        print("Отсортированный массив:", *numbers)
        print(f"Сравнений: {comparisons}. Обменов: {swaps}.")
