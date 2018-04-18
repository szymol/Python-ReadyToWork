with open('tabliczka.txt','w') as wyjscie:
    # int(i) = 1
    wynik = 1
    for i in range(0,101):
        wyjscie.write(str(i))
        wyjscie.write(',')
    wyjscie.write('\n')
    for k in range(1, 101):
        wyjscie.write(str(k)+',')
        for j in range(1,101):
            wynik = k * j
            wyjscie.write(str(wynik)+',')
        wyjscie.write('\n')
