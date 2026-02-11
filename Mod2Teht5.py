leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#Luotigrammoina = 13.3
#NaulaLuoteina = 32
#LeiviskaNauloina = 20

kaikki_luodit = (leiviskat*20*32+naulat*32+luodit)

grammat=kaikki_luodit*13.3

kilot=int(grammat//1000)
loput_grammat=grammat%1000

print(f"{kilot} Kiloa ja {loput_grammat} Grammaa")


