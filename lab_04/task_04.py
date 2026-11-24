def is_palindrome(text):
    def compare(left, right):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return compare(left + 1, right - 1)

    return compare(0, len(text) - 1)


# Идём с двух концов строки навстречу друг другу. До середины хватает.
if __name__ == "__main__":
    text = input("Строка: ")
    if is_palindrome(text):
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")
