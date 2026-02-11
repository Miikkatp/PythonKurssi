hytti = int(input("Hyttiluokat ovat numeroitu seuraavasti (Lux=1, A=2, B=3, C=4)."
                  " Ilmoita hyttiluokkasi numerolla "))
if hytti==1:
    print("Hyttisi on parvekkeellinen yläkannella")
elif hytti==2:
    print("Hyttisi on ikkunallinen autokannen yläpuolella")
elif hytti==3:
    print("Hyttisi on ikkunaton autokannen yläpuolella")
elif hytti==4:
    print("Hyttisi on ikkunaton autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")
