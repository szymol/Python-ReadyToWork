rok = int(input("podaj rok: "))

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    print("rok jest przestepny")


else:
    print("rok jest nie przestepny")