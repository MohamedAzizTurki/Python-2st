PF = float(input("Donner SVP le prix de fabrication: "))
PV = float(input("Donner SVP le prix de vente: "))
if PV>PF:
    print("Profit")
elif PV<PF:
    print("Perte")
else:
    print("Ni profit ni perte")