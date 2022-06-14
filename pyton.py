print("Pierwsze równanie")
x1 = int(input("Podaj x: "))
y1 = int(input("Podaj y: "))
w1 = int(input("Podaj wynik: "))

print("Drugie równanie")
x2 = int(input("Podaj x: "))
y2 = int(input("Podaj y: "))
w2 = int(input("Podaj wynik: "))

W = x1 * y2 - x2 * y1
Wx = w1 * y2 - w2 * y1
Wy = x1 * w2 - x2 * w1

x = Wx/W
y = Wy/W

print(f"x = {x}")
print(f"y = {y}")