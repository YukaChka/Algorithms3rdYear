from decimal import Decimal


def insertion_sort(numbers):
    """Сортирует список на месте и возвращает число исходных инверсий."""
    inversions = 0

    for i in range(1, len(numbers)):
        current = numbers[i]
        position = i

        while position > 0 and numbers[position - 1] > current:
            numbers[position] = numbers[position - 1]
            position -= 1

        numbers[position] = current
        # Каждый сдвиг исправляет одну пару, которая стояла в обратном порядке.
        inversions += i - position

    return inversions


if __name__ == "__main__":
    line = input("Введите числа через пробел (Enter — пример с цифрами π): ")
    if line.strip():
        numbers = list(map(Decimal, line.split()))
    else:
        numbers = [int(digit) for digit in "3141592653589793"]

    print("Исходный массив:", *numbers)
    inversions = insertion_sort(numbers)
    print("Отсортированный массив:", *numbers)
    print("Инверсий в исходном массиве:", inversions)
