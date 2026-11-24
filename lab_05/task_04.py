numbers = list(map(float, input("Элементы массива через пробел: ").split()))

# Два указателя идут навстречу. Если встретятся на одном элементе, берём его один раз.
result = []
left = 0
right = len(numbers) - 1
while left < right:
    result.append(numbers[left])
    result.append(numbers[right])
    left += 1
    right -= 1

if left == right:
    result.append(numbers[left])

print(*result)
