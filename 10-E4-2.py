n = int(input("Donner SVP un nombre: "))
d1 = int(input("Donner SVP le diviseur 1: "))
d2 = int(input("Donner SVP le diviseur 2: "))
if((n%d1==0)and(n%d2==0)):
    print(n ,"est divisible sur", d1 ,"et",d2)
else:
    print(n ,"n'est pas divisible sur", d1 ,"et",d2)