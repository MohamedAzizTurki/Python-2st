N = float(input("Donner SVP la note de l'étudiant: "))
if N==10 :
	print("Passable")
elif N>10 and N<13:
 	print("Assez Bien")
elif N>=13 and N<15:
 	print("Bien")
elif N>=15 and N<20:
 	print("Trés Bien")
elif N>=20:
	print("Génie")
else:print("Redouble")