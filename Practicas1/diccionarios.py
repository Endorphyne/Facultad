import os
#   DICCIONARIOS
#   el caso de uso es cuando no buscamos usar indices numericos si no indices de tipo cadena por ej
# agenda = {
#     'juan'  :   380,
#     'sonia' :   379,
#     'pepe'  :   312, 
# }
# agenda['anita'] = 123
#   metodos para acceder a items en los diccionarios
#   print(agenda['juan'])
#   print(agenda.get('juan'))
#   podemos usar 'del' para eliminar un item en el diccionario ej: del agenda['sonia']
#   podemos revisar si tenemos una clave en el diccionario con 'in'
#   podemos obtener las llaves con el metodo '.keys'
#   podemos ordenar con el metodo 'sorted()'
#   y para que este al revez ponemos reverse=True como segundo valor al sorted
#   para obtener los valores solamente podemos usar ".values()"
#   para obtener los items usamos el metodo '.items()' //IMPORTANTE// este metodo devuelve un par de clave|valor 
#   Para copiar el diccionario podemos usar el metodo '.copy' o el metodo 'dict()' 
#   =============================================================================================================================
#   EJERCICIOS
#   Ejercicio 1 
# Teniendo los siguientes conjuntos: 
# primera_canasta: papa’ ‘zapa
# llo’, ‘zanahoria’, ‘rábano’, ‘lechuga’, ‘tomate’, ‘papa’ segunda_canasta: ‘tomate’, ‘lechuga’, ‘arveja’, ‘choclo’, ‘mandioca’, ‘lechuga’ Se pide imprimir: 
# a) La longitud de cada conjunto. 
# b) Si el elemento ‘arveja’ se encuentra en cada conjunto. 
# c) Si el elemento ‘tomate’ se encuentra en cada conjunto. 
# d) Los elementos de la primera_canasta. 
# e) Los elementos de la segunda_canasta. 
# f) Los elementos que se encuentran en la primera_canasta, pero no en la  segunda_canasta. 
# g) Los elementos que se encuentran tanto en la primera_canasta como en la segunda_canasta. 
# h) Los elementos que se encuentran en la primera_canasta o en la segunda_canasta. i) Los elementos que se encuentran en la primera_canasta o en la segunda_canasta, pero  no en ambos. 
# Ejercicio 2 
# Crear tres conjuntos llamados primero, segundo y tercero; agregar en cada uno el nombre de  las materias de la carrera sin los números (en primero debería estar la materia “Practicas”, al  igual que en segundo y tercero). Mostrar cuales materias son propias de cada año (no se  repiten en los demás conjuntos) y aquellas que se repiten en 2 o en 3 conjuntos. 
# Ejercicio 3 
# Teniendo el siguiente diccionario: 
# meses = {‘enero’: 31, ‘febrero’: 28, ‘marzo’: 31, ‘abril’: 30, ‘mayo’: 31, ‘junio’: 30, ‘julio’:  31, ‘agosto’: 31, ‘septiembre’: 30, ‘octubre’: 31, ‘noviembre’: 30} 
# Se pide: 
# a) Imprimir la cantidad de días de enero. 
# b) Imprimir la cantidad de días de junio. 
# c) Imprimir la cantidad de días de febrero. 
# d) Imprimir si existe la clave ‘noviembre’.
# e) Imprimir si existe la clave ‘domingo’ 
# f) Imprimir el listado de los nombres de los meses. 
# g) Imprimir el listado de los nombres de los meses ordenados alfabéticamente. h) Cambiar la cantidad de días de febrero de 28 a 29. 
# i) Agregar al diccionario la cantidad de días de diciembre. 
# j) Imprimir el diccionario completo con el siguiente formato: ‘El mes enero tiene 31 días’. 
# Ejercicio 4 
# Crear un programa que permita a un usuario ingresar un diccionario de libros preferidos. El  usuario deberá ingresar una clave y la descripción del mismo, hasta que indique que no desea  seguir ingresando libros. Imprimir el diccionario final con el siguiente formato: ‘El libro Martín  Fierro tiene la clave MF’.
#===================================================================================================================================================================
#EJERCICIO 1
# primera_canasta={ 'papa', 'zapallo', 'zanahoria', 'rábano', 'lechuga', 'tomate', 'papa'} 
# segunda_canasta={ 'tomate', 'lechuga', 'arveja', 'choclo', 'mandioca', 'lechuga' }
# print(len(primera_canasta)) # A
# print(len(segunda_canasta)) # A
# print('arveja' in primera_canasta)    #   B
# print('arveja' in segunda_canasta)    #   B
# comparativa = primera_canasta & segunda_canasta 
# print ('tomate' in comparativa)   #   C
# for x in primera_canasta :    #   D
#     print(x)
# for i in segunda_canasta :    #   E
#     print(i)
# print(primera_canasta - segunda_canasta)    #   F
# print(primera_canasta&segunda_canasta)  #   G
# print(primera_canasta|segunda_canasta)  #   H
# print(primera_canasta^segunda_canasta)  #   I
#=====================================================================================================
#EJERCICIO 2
# primero =   {'Practicas','Matematica','arquitectura','Programacion logica','Elementos de contabilidad','programacion','taller de informatica','Sistemas operativos','Ingles Tecnico'}
# segundo =   {'Practicas','programacion','Analisis y diseño de sistemas','base de datos','Programacion logica','Matematica','Principios de administracion y organizacion','Redes de computadoras','Tecnicas del lenguaje y la comunicacion','estadisticas'}
# tercero =   {'Practicas','Investigacion operativa','Practica Profesional','Investigacion operativa','Etica y deontologia profesional','programacion','desarrollo de aplicaciones web','seminario de la practiva'}
# materias_unicas_primero = (primero-segundo)
# materias_unicas_primero.union(primero-tercero)
# print('Materias de primero: ',materias_unicas_primero)
# materias_unicas_segundo = (segundo-primero)
# materias_unicas_segundo.union(segundo-tercero)
# materias_unicas_tercero = (tercero-primero)
# materias_unicas_tercero.union(tercero-segundo)
# print('Materias de segundo: ',materias_unicas_segundo)
# print('Materias de tercero: ',materias_unicas_tercero)
# materias_repetidas = primero|segundo
# materias_repetidas = materias_repetidas|tercero
# print('Las materias repetidas son: ',materias_repetidas)
#=======================================================================================================================================================================
#EJERCICIO 3
# meses = {
# 'enero': 31, 
# 'febrero': 28, 
# 'marzo': 31, 
# 'abril': 30, 
# 'mayo': 31, 
# 'junio': 30, 
# 'julio':  31,
# 'agosto': 31,
# 'septiembre':30, 
# 'octubre': 31, 
# 'noviembre': 30}
# print(f'Enero tiene {meses["enero"]} dias')
# print(f'Junio tiene {meses["junio"]} dias')
# print(f'Febrero tiene {meses["febrero"]} dias')
# print('noviembre' in meses)
# print('domingo' in meses)
# print(sorted(meses))
# meses['febrero'] = 29 
# meses['Diciembre'] = 31
# for x,y in meses.items():
#     print(f'El mes de {x} tiene {y} dias')
#=======================================================================================================================================================================
# EJERCICIO 4
libreria = {}
opcion = " "
while opcion != '0' : 
    os.system("cls")
    opcion =input(f"""Su libreria tiene: {len(libreria)} libros
                    Seleccione la opcion a realizar: 
                    1-Ingresar un libro
                    0-Salir 
                    : """)
    if opcion == '1' :
        libreria.update({input("Introduza el titulo del libro: "):input('Introduzca una descripcion del libro: ')})
    elif opcion == '0':
        for x in libreria.keys():
            y = x
            y = y.upper()
            libro = y.split()
            codigo = ""
            for i in libro:
                codigo += i[0]
            print(f"El libro {x} tiene la clave: {codigo}")
    else:
        print("Valor invalido")