M1 = float(input("Donner SVP la note de la premiere matière: "))
M2 = float(input("Donner SVP la note de la deuxième matière: "))
M3 = float(input("Donner SVP la note de la troisième matière: "))
M4 = float(input("Donner SVP la note de la quatrième matière: "))
M5 = float(input("Donner SVP la note de la cinquième matière: "))

T = M1+M2+M3+M4+M5

if M1<0 or M1>20 or M2<0 or M2>20 or M3<0 or M3>20 or M4<0 or M4>20 or M5<0 or M5>20:
	print("Impossible")
else:
	print("Le totale =" ,T)
	print("La moyenne =" ,T/5)
	print("Le pourcentage =" ,((T/5)*100)/20,"%")