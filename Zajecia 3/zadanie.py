with open('plik.txt') as plik:
# pierwsza = plik.readline()
# print(pierwsza)
#upper do zamieniania malyliter na wilekie
    for linia in plik:
       print(linia[:-1])
