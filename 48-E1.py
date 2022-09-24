N = int(input("Saisir un entier: "))
etat=True
if N>0:
    ch = str(N)
for lettre in ch:
    if ch.count(lettre)>1:
        etat=False
        break
if etat==True:
    print(N,"est distincte")
else: print(N,"est non distincte") 