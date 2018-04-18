with open('test_pisania.txt','r') as plik, open('test.txt','w') as wyjscie:
    zmienna = 0

    for linia in plik:
        if zmienna % 3 == 0:
            wyjscie.write('********\n')
        else:
            if 'kocham' in linia:
                wyjscie.write('*****')
            elif 'Kocham' in linia:
                wyjscie.write('*****')
            else:
                wyjscie.write(linia)
        zmienna = zmienna + 1