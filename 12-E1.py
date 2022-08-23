# Algorithme voyelle
l = input("Donner SVP un létre: ")
if (l=='a' or l=='e' or l=='i' or l=='o' or l=='u' or l=='A' or l=='E' or l=='I' or l=='O' or l=='U'):
    print(l ,"est un voyelle")
elif ((l>='a' and l<='z')or(l>='A' and l<='Z')):
    print(l ,"est un consonne")
else:
    print(l ,"est un caractére")