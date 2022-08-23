ch = input("Donner SVP un caractére: ")
if (ch>='a' and ch<='z')or(ch>='A' and ch<='Z'):
    print(ch, "est un lettre")
elif ch>='0' and ch<='9':
    print(ch, "est un chiffre")
else:
    print(ch ,"est un caractére spésyale")