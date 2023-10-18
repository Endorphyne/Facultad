minEmpleado = 10
minFacturacion = 2 #millones
minBalance = 2 #millones
#datos empresa
empleados = 20
facturacion = 18 #millones 
balance = 5 #millones 
#pyme
esPyme = empleados < minEmpleado and facturacion<minFacturacion or balance<minBalance
print ("es pyme", esPyme)
print (type(esPyme))
esPequeña = not esPyme and (balance <= 10 or empleados <=50 and facturacion <= 10)
print("es pequeña ", esPequeña)
print(type(esPequeña))