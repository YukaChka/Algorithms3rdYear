from decimal import Decimal


def binary_search(numbers, target, checked=None):
    """Возвращает индекс найденного элемента или -1."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        # Проверяем середину и вычёркиваем сразу половину оставшихся кандидатов.
        middle = (left + right) // 2
        value = numbers[middle]
        if checked is not None:
            checked.append(middle)

        if value == target:
            return middle
        if value > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


if __name__ == "__main__":
    numbers = list(map(Decimal, input("Введите числа по возрастанию через пробел: ").split()))
    target = Decimal(input("Введите искомое число: "))

    checked = []
    index = binary_search(numbers, target, checked)
    print("Индекс (с нуля, -1 если не найден):", index)
    print("Проверено элементов:", len(checked))
