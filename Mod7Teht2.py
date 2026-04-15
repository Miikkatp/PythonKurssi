annetutnimet = set()

while True:
    nimi = input("Anna nimi, kun haluat lopettaa, älä laita mitään :) : ")

    if nimi == "":
        break

    if nimi in annetutnimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        annetutnimet.add(nimi)

print("\nSyötetyt nimet:")
for nimi in annetutnimet:
    print(nimi)