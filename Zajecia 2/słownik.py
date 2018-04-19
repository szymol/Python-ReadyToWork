wejscie = input('Podaj slowo: ')

slownik = {'czerwony':'red', 'niebieski':'blue', 'tak':'yes', 'nie':'no', 'rower':'bike', 'home':'dom', 'klucz':'key', 'mysz':'mouse', 'pies':'dog', 'kot':'cat'}

#print(slownik)

if wejscie in slownik:
    print(wejscie, slownik[wejscie])
else:
    print("nie ma wyrazu w slowniku")