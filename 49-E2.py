ch = input("Saisir une chaine SVP: ")
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Voy = "AEIOUY"
pos=1
poids=0
for lettre in ch:
    if lettre in Voy:
        poids+=pos*(Alpha.find(lettre)+1)
    pos+=1
print("Le poids =",poids)