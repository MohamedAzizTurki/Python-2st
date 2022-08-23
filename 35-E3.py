n = int(input("Saisir un entier: "))
etat=True
if n>0:
    ch=str(n)
for lettre in ch:
    if ch.count (lettre)>1:
        etat=False
        break
if etat==True:
    print("Distinct")
else:print("Non Distinct")