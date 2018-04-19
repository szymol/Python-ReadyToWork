print('Lista kwadratów liczb naturalnych z przedziału [0,50]')
print ([x ** 2 for x in range(0,50)])
print('\n')

print("sześciany liczb naturalnych z zakresu 20 do 30")
print ([y ** 3 for y in range(20,31)])
print('\n')

print('wartości funkcji 3x-2 na liczbach całkowitych przedziale od -5 do 5')
print([(3*z - 2) for z in range(-5,6)])
print('\n')

print('pary (x,y), gdzie x jest liczbą naturalną z zakresu 10-20, a y liczbą naturalną z zakresu 5-10')
z1 = [a for a in range(10,21)]
z2 = [b for b in range(5,11)]
print([(a,b) for a in z1 for b in z2])
print ('\n')

print("Lista par (x,y), gdzie x jest liczbą całkowitą z przedziału [4,7], a y jednym z napisów 'jabłko', 'gruszka' lub 'komputer'")
x1=[ c for c in range(4,8)]
x2= ['jablko', 'gruszka', 'kommputer']

print([(c,d) for c in x1 for d in x2])

