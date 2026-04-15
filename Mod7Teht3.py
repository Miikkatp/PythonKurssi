lentoasemat = {}

while True:
    valinta = input("Valitse (1=lisää, 2=hae, 3=lopeta): ")

    if valinta == "1":
        icao = input("ICAO-koodi: ")
        nimi = input("Nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "2":
        icao = input("ICAO-koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Ei löytynyt")

    elif valinta == "3":
        break

    else:
        print("Virheellinen valinta")