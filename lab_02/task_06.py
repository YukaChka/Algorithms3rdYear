n = int(input("Число от 1 до 999: "))

# Количество цифр видно по границам 10 и 100.
if n < 10:
    digits = "однозначное"
elif n < 100:
    digits = "двузначное"
else:
    digits = "трехзначное"

if n % 2 == 0:
    parity = "четное"
else:
    parity = "нечетное"

print(parity, digits, "число")
