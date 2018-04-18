import sys
with open('plik.txt') as plik:
    zmienna = 0
    for linia in plik:
        #print(zmienna)
        male = linia.lower()
        # print('calosc zamienienona na male liter: ',male)
        #print(male)
        sys.stdout.write(male[:-1]+male[-6:])
        zmienna = zmienna + 1
