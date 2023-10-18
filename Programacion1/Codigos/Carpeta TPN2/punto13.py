materias = {}
for x in range(int(input('Introduzca la cantidad de materias de su cursado: '))):
    materia = str(input('Introduzca la materia: ')) 
    nota = float(input('introduzca la nota de {}: '.format(materia)))
    materias.update({materia:nota})
print('Las notas de cada materia son: ')
for i in materias.items() : 
    print(i[0],i[-1])
