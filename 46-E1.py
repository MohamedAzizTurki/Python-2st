n = int(input("Donner un entier composer de trois chiffre SVP: "))
ch=str(n)
S = int(ch[0])+int(ch[1])+int(ch[2])
P = int(ch[0])*int(ch[1])*int(ch[2])
if P%S==0:
    print(n,"vérifive la propiété")
else: print(n,"ne vérifive pas la propiété")