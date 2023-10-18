materias = []
cantidad_materias = int(input('Ingrese la cantidad de materias a almacenar: '))
for x in range(cantidad_materias) : 
    materias.append(str(input('Introduzca la materia: ')))
lista = ', '.join(materias)
print('Yo estudio {}'.format(lista))