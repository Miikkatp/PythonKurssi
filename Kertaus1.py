tuntipalkka = float(input("Syötä tuntipalkka: "))
tunnit = float(input("syötä tunnit: "))
viikonpaiva = (input("Syötä viikonpaiva: "))

if viikonpaiva == "sunnuntai":
    palkka = tuntipalkka * tunnit * 2
elif viikonpaiva != "sunnuntai":
    palkka = tuntipalkka * tunnit
else:
    palkka = 0

    print("Päivän palkka:", palkka, "euroa")
