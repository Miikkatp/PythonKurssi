luku = int(input("Anna kokonaisluku: "))

if luku / 15 == luku // 15:
    print("jaolinen molemmilla luvuilla!")
elif luku / 3 == luku // 3:
    print("kolmela jaollinen")
elif luku / 5 == luku // 5:
    print("viidellä jaollinen")
else:
    print("Ei ole jaollinen")