import math

Kanta_str = input("Kerro suorakulmion kanta ")
kanta = float(Kanta_str)
Korkeus_str = input("Kerro suorakulmion korkeus ")
korkeus = float(Korkeus_str)

piiri = (korkeus*2+kanta*2)
pintaala = (kanta*korkeus)
print("Suorakulmion piiri on, " + str(piiri), "Ja Suorakulmion pinta-ala on " + str(pintaala))

