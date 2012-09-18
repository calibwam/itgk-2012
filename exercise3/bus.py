def prices(age):
    if age < 0:
        print("FREAK!")
    elif age < 5:
        print("Gratis")
    elif age < 15:
        print("10 kr")
    elif age < 20:
        print("20 kr")
    elif age < 25:
        print("30 kr")
    elif age < 60:
        print("40 kr")
    else:
        print("Gratis")

prices(3)
prices(9)
prices(19)
prices(23)
prices(33)
prices(63)
