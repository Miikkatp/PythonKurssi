Sukupuoli=int(input("Ilmoita sukupuolesi numerolla, 1=Mies 2=Nainen: "))
Hemoglobiini=float(input("Ilmoita hemogoblini arvosi (g/l): "))
if Sukupuoli==1:
    if Hemoglobiini <134:
        print("Hemoglobiini arvosi on matala")
    elif Hemoglobiini <= 195:
        print("Hemoblobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi on korkea")

elif Sukupuoli==2:
    if Hemoglobiini <117:
        print("Hemoglobiini arvosi on matala")
    elif Hemoglobiini <=175:
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi on korkea")

else:
    print("Virheellinen sukupuoli. Valitse sukupuoli 1=Mies, 2=Nainen")