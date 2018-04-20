import re

kod_pocztowy = input('Podaj kod pocztowy: ')
dopasowanie = re.match(r'^[0-9]{2}\-[0-9]{3}$', kod_pocztowy)
if dopasowanie:
    print('OK')
else:
    print('Blad')

nr_tel = input('Podaj nr telefonu: ')
dopasowanie2 = re.match(r'^([0-9]{9})|([0-9]{10})|(\+?[0-9]{11})$',nr_tel)
if dopasowanie2:
    print('OK')
else:
    print('Blad')

mail = input('Podaj adres e-mail: ')
dopasowanie3 = re.match(r'^[a-z0-9\.]{1,}\@([a-z0-9]{1,}\.){1,}[a-z]{1,}$', mail)
if dopasowanie3:
    print('OK')
else:
    print('Blad')