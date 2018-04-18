#split
with open('zliczanie.txt') as liczba:
    liczba_lini=0
    liczba_slow = 0
    liczba_znakow = 0
    for line in liczba:
        liczba_lini= liczba_lini + 1
        liczba_znakow = liczba_znakow + len(line)
        liczba_slow = liczba_slow + len(line.split())
    print('Liczba linii: ',liczba_lini)
    print('Liczba znakow: ',liczba_znakow)
    print('Liczba slow: ', liczba_slow)