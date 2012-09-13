def main():
    name = input("Navnet på bilen: ")
    gross_price = float(input("Bruttopris: "))
    weight = float(input("Vekt: "))
    hp = float(input("Antall hestekrefter: "))
    co2 = float(input("CO2-utslipp: "))
    volume = float(input("Motorolum: "))

    calculate_price(name, gross_price, weight, hp, co2, volume)

def calculate_price(name, gross_price, weight, hp, co2, volume):
    weightp = gross_price * weight * 0.00034
    hpp = gross_price * hp * 0.00015
    co2p = gross_price * co2 * 0.004
    volumep = gross_price * volume * 0.00055
    net_price = weightp + hpp + co2p + volumep

    print("Utsalgspris på %s vil bli %.2f" % (name, net_price))

main()
