A = int(input("Donner SVP l'année: "))
if (A%4==0 and A%100!=0) or A%400==0:
    print(A, "est une année bisécstile")
else:
    print(A, "est une année simple")