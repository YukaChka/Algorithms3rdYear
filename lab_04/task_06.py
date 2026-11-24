def reverse_words(text):
    words = text.split()

    def swap_words(left, right):
        if left >= right:
            return
        words[left], words[right] = words[right], words[left]
        swap_words(left + 1, right - 1)

    swap_words(0, len(words) - 1)
    return " ".join(words)


# Меняем местами крайние слова и передаём рекурсии то, что осталось между ними.
if __name__ == "__main__":
    text = input("Строка: ")
    print("Обратный порядок слов:", reverse_words(text))
