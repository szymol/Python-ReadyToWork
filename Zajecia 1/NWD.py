a = int(input("Podaj pierwsza wartosc: "))
b = int(input("Podaj druga wartosc: "))

while b:
    a, b = b, a % b
print("NWD =",a)