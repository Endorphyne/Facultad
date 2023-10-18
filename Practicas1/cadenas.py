#Caracteristicas de las cadenas
#cada caracter tiene un indice que empieza en 0 y va hasta el -1
#se pueden separar en subcadenas usando []
#Son inmutables, si queremos alterar una cadena debemos definir una nueva alterando la nueva conforme nuestras necesidades
#EJEMPLOS PARA ALTERAR CADENAS
#cadena = "Hola"
#nueva_cadena = cadena.upper()
#nueva_cadena = "h" + cadena[1]
#nombre = "Juan"
#edad = 20
#apellido = "Gomez"
#para combinar estas cadenas hay 4 opciones
#PRIMERA OPCION
#Usar el operador de + o , 
#SEGUNDA OPCION
#usar el operador de %, que con cadenas funciona como un concatenador 
#print("hola %s %s"%(nombre,apellido))
#TERCERA OPCION
#Usar el operador de format
#similar al operador de % pero con llaves dentro 
#print("hola {1} {0}".format(nombre,apellido))
#CUARTA OPCION
#cadenas de formato f
#se le pueden pasar directamente la variable en donde la necesitamos 
#print(f"Hola {nombre} {apellido}")
#METODO PARA INGRESAR DATOS AL CODIGO
#input, sirve para que el usuario ingrese un dato al codigo, lo ingresado es siempre una cadena 