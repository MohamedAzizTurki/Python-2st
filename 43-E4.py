N = int(input("Saisir SVP un nombre: "))
etat=True
for i in range(2,N-1):
    if N%i==0:
        etat = False
        break
if etat==True:
    print(N,"est un nombre premier")
else:
    print(N,"n'est pas un nombre premier")
