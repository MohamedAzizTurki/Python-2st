N = int(input("Saisir un nombre SVP: "))
for i in range(2,N-1):
    if N%i==0:
        print(i,"est un diviseur de",N)
