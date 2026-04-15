Vuodenaika = ("talvi", "Talvi", "kevät", "Kevät", "kevät", "kesä," , "kesä", "kesä", "Syksy", "Syksy"
              , "Syksy", "Talvi")

kuukausi=int(input("anna haluamasi kuukauden numero: "))

if 1<= kuukausi <=12:
    print("Vuodenaika kuukaudellasi on", Vuodenaika[kuukausi - 1])

else: print("Anna oikean kuukauden numero")

