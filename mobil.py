print("Välkommen till Lars och Olof mobilabonnemang")
uppskattade_minuter = int(input("Hur många minuter uppskattar du att du ringer?: "))

if uppskattade_minuter <= 33:
    print("Det abonnemang som passar dig bäst är Kontant.")
elif uppskattade_minuter > 33 and uppskattade_minuter < 66:
    print("Det abonnemang som passar dig bäst är Normal.")
if uppskattade_minuter < 99:
    print("Bra, du behöver ett plus abonnemang.")

if uppskattade_minuter > 999:
    print("Du behöver µbér abonnemang... du har just nu ultra abonnemanget.")
elif uppskattade_minuter < 999 and uppskattade_minuter > 99:
    print("Du är på gränsen till de ultimata abonnemanget.")