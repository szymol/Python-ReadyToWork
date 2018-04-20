import matplotlib.pyplot as plt
amex = 0
diners = 0
mastercard = 0
visa = 0
licznik = 0
with open('SalesJan2009.csv') as plik:
    for line in plik:
        tablica = line.split(',')
        if licznik >=1:
            if tablica[3] == 'Visa':
                visa = visa + int(tablica[2])
            elif tablica[3] == 'Amex':
                amex = amex + int(tablica[2])
            elif tablica[3] == 'Diners':
                diners = diners + int(tablica[2])
            elif tablica[3] == 'Mastercard':
                mastercard = mastercard + int(tablica[2])
        licznik = licznik + 1

labels = 'Amex', 'Diners', 'Mastercard', 'Visa'
sizes = [amex, diners, mastercard, visa]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()