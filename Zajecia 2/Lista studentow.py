a = ('Alex', 'Szymczak', [3.5,4,5])
b = ('Arek', 'Adiusz', [4.5,4,4])
c = ('Jan', 'Kowalski', [2,2,2])

lista = [a,b,c]

for i in lista:
    if (i[2][0] + i[2][1] + i[2][2]) / 3 > 4:
        print(i[0:2])