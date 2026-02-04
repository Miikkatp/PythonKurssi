
Ekaluku_str = input("Kirjoita ensimmäinen kokonaisluku ")
ekaluku = float(Ekaluku_str)
Tokaluku_str = input("Kirjoita toinen kokonaisluku ")
tokaluku = float(Tokaluku_str)
Kolmasluku_str = input("Kirjoita kolmas kokonaisluku ")
kolmasluku = float(Kolmasluku_str)

summa = (kolmasluku+ekaluku+tokaluku)

tulo = (kolmasluku*ekaluku*tokaluku)

keskiarvo = ((kolmasluku+ekaluku+tokaluku)/3)

print("Lukujen summa on " +str(summa), ", Lukujen tulo on " +str(tulo), "Ja Lukujen keskiarvo on " +str(keskiarvo) )
