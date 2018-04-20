import re
with open('przykladowy_tekst.txt',encoding="UTF-8") as plik, open('poprawiony_tekst.txt','w',encoding="UTF-8") as wyjscie:
     for linia in plik:
        zmieniony = re.sub(r'óje\b', r'uje', linia)

        zmieniony = re.sub(r'(b|p|d|k|g|ch|j|w)ż', r'\1rz',zmieniony)

        zmieniony = re.sub(r'h\b', r'ch', zmieniony)
        wyjscie.write(zmieniony)
