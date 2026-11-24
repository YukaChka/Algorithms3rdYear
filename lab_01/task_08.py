a = float(input("Координата A: "))
b = float(input("Координата B: "))
c = float(input("Координата C между A и B: "))

# Даже если A правее B, обе длины берём положительными.
ac = abs(c - a)
bc = abs(c - b)

print("Произведение длин:", ac * bc)
