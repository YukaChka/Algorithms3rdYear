def bubble_sort(numbers):
    """Сортирует список по возрастанию на месте."""
    end = len(numbers) - 1

    while end > 0:
        last_swap = 0
        for right in range(1, end + 1):
            left = right - 1
            if numbers[left] > numbers[right]:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                last_swap = left

        # Пузырёк запоминает, где ему в последний раз пришлось вмешаться.
        end = last_swap


if __name__ == "__main__":
    numbers = list(map(float, input("Введите числа через пробел: ").split()))
    bubble_sort(numbers)
    print("Отсортированный массив:", *numbers)
