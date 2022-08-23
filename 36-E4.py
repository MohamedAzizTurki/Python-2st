N = int(input("Enter un entier C: "))
ch=str(N)
S=0
P=1
for lettre in ch:
    S=S+int(lettre)
    P=P*int(lettre)
if P%S==0:
    print("Divisible")
else: print("Non divisible")
