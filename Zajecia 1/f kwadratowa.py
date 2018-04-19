import math

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

(delta) = (b**2 - 4*a*c)

if delta < 0:
    print("brak rozwiazań")
elif delta == 0:
    x0=(-b)/2*a
    print(x0)
else:
    x1 =((-b) - math.sqrt(delta))/2*a
    x2 =((-b) + math.sqrt(delta))/2*a
    print(x1,x2)