import re

tekst = 'Adam to hultaj nicpoń i gagatek i hultaje hultajowi'

zmieniony = re.sub(r'(hulta([a-ź]*)|nicpo([a-ź]*)|gagat([a-ź]*))', r'*****', tekst)
print(zmieniony)