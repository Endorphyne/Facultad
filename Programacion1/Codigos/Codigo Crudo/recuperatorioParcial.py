menuBebidas = {} #menu donde se cargaran las bebidas del pedido 
menuComidas = {} #menu donde se cargaran las comidas del pedido
import os #biblioteca de comandos cmd
salida = 100 #condiciones irreales para evitar corte de bucle accidental
bebida = 100
comida = 100
while salida != 0 :#condicion de corte para el bucle
	operacion = input('''
	Menu Principal
	-----------------------------
	1. Mostrar Lista de Precios
	2. Ingresar Bebidas
	3. Ingresar comidas
	0. Salir
	-----------------------------
	OPERACION : ''')#layout del mnenu
	if operacion == '2' :
		while bebida != 0:#bucle para agregar items
			bebida = input("Ingrese una bebida (0 finaliza): ")
			bebida = bebida.upper()
			if bebida != '0':#revisa que no se quiera dejar de cargar bebidas
				precio = input('Ingrese el precio de {bebida}: $'.format(bebida=bebida))
				menuBebidas[bebida] = precio #carga de las bebidas junto al precio al menu
			else :
				bebida = 0#establece la salida 
				os.system('cls')
	elif operacion == '3' :
		while comida != 0:#bucle para ingresar items
			comida = input('Ingrese una comida (0 finaliza): ')
			comida = comida.upper()
			if comida != '0':#revisa la condicion de corte
				precio2 = input('Ingrese el precio de {comida}: $'.format(comida=comida))
				menuComidas[comida] = precio2
			else :
				comida = 0  #corta el bucle
				os.system('cls')
	elif operacion == '1':#imprime el menu
		print('''	 	
		Lista de Precios
		----------------
		Bebidas
		-------''')
		for item, value in menuBebidas.items():
			print('''
			{bebida}	$ {precio}'''.format(bebida=item,precio=value))#layout del menu de bebidas
		print('''
	 	Comidas
	 	--------------------------''')
		for item2, value2 in menuComidas.items():
			print('''
			{comida}	$ {precio2}'''.format(comida=item2,precio2=value2))#Layout del menu de comidas
		espera = input('Presiona ENTER para continuar')
	elif operacion == '0':#sale del codigo/menu
		salida = 0 
	else :
		print('Operacion invalida')
		os.system('cls')