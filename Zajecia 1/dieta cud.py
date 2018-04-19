waga = float(input('podaj wage w kg: '))
wzrost = float(input('podaj wzrost w m: '))

bmi = float (waga/(wzrost**2))
print("BMI: ", bmi)
if 25<= bmi < 30:
    print("nadwaga")
elif bmi >= 30:
    print("otyłość")
else:
    print("BMI w normie")