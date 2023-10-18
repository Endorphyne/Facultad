agenda = {
    'Rogelio':3755777342,
    'Lautaro':3755797830
}
eleccion = str(input('''
AGENDA----
1 - Agregar una persona.
2 - Buscar un telefono 
x - Salir
Ingrese una opción(1/2/x):'''))
if eleccion == '1' :
    nombre = str(input('Introduzca un nombre: '))
    if nombre in agenda:
        siguiente = input('El nombre esta repetido presione enter para continuar')
        siguiente = 'ENTER'
    else : 
        numero = int(input('Introduzca el numero de {}'.format(nombre)))
        agenda.update({nombre:numero})
if eleccion == '2' :
    nombre = str(input('Ingrese que nombre desea buscar: '))
    if nombre in agenda:
        print('El numero de {nombre} es: {numero}'.format(nombre=nombre,numero=agenda[nombre][0]))
if eleccion == 'x' : 
    print('Su agenda:',agenda)
print(agenda)