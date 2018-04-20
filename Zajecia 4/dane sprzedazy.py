with open('SalesJan2009.csv') as plik:
    licznik = 0
    najw_trnasakcja = 0
    suma_visa = 0
    srednia_bryt = 0
    liczba_slow = 0
    licznik_bryt = 0

    for line in plik:
        tablica = line.split(',')
        if licznik > 1:
            if najw_trnasakcja < int(tablica[2]):
                najw_trnasakcja = int(tablica[2])
            elif tablica[3] == 'Visa':
                suma_visa = suma_visa + int(tablica[2])
            elif tablica[7] == 'United Kingdom':
                srednia_bryt = srednia_bryt + int(tablica[2])
                licznik_bryt = licznik_bryt + 1
        licznik = licznik + 1
    print('Największa transakcja: ', najw_trnasakcja)
    print('Suma transakcji Visa: ', suma_visa)
    print('suma bryt: ', srednia_bryt)
    srednia_bryt = srednia_bryt / licznik_bryt
    print('licznik: ', licznik_bryt)
    print('Średnie wydatki Brytyjczyków: ', srednia_bryt)