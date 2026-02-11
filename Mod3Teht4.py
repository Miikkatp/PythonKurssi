vuosiluku=int(input("Anna vuosiluku, niin kerron onko se karkausvuosi: "))
if vuosiluku % 4==0:
    if vuosiluku % 100==0:
        if vuosiluku % 400==0:
            print("Antamasi vuosi on karkausvuosi!")
        else:print("Antamasi vuosi ei ole karkausvuosi!")
    else:print("Antamasi vuosi ei ole karkausvuosi!")
else:print("Antamasi vuosi ei ole karkausvuosi!")
