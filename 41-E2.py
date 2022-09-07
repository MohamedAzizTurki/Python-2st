m = int(input("Donner les minutes: "))
h = int(input("Donner les heures: "))
T1 = h*60+m+1
T2 = T1//60
T3 = T1%60
if T2>=60:
    print(T2,"minutes")
elif T2<=60:
    print(T2,"heures","est",T3,"minutes")