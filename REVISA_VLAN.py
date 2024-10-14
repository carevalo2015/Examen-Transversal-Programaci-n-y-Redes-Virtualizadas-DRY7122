n_vlan = int(input("Ingrese el número de la VLAN: "))
while n_vlan > 4096:
	print("Número de VLAN no válido")
	n_vlan = int(input("Ingrese un número de VLAN válido: "))
else:
	if n_vlan <= 1005:
		print("El número de VLAN ingresado corresponde al rango normal")
	else:
		print("El número de VLAN ingresado corresponde al rango extendido")

