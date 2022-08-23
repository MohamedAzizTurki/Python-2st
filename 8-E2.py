T = float(input("Donner SVP la température de l'eau:"))
if (T<0):
	print('Solide')
elif (T>0) and (T<100):
	print('Liquide')
else:
	print('Vapeur')