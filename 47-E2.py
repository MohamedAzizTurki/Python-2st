N = int(input("Donner un nombre: "))
etat=True
for i in range(N):
    S=i
    M=str(i)
    for j in M:
        S+=int(j)
    if S==N:
        etat=False
        break
if etat==False:
    print(N,"n'est pas un auto-nombre")
else: print(N,"est un auto-nombre")