materias = []

for x in range(int(input('introduzca la cantidad de materias: '))):
    if x == 0: 
        print('Introduzca las materias')
    materias.append(input())
i = 0
while i < len(materias) :
    notas = float(input('Introduzca la nota de la materia {}: '.format(materias[i])))
    if notas >= 6 and notas <= 10 : 
        print('{} aprobada.'.format(materias[i]))
        materias.pop(i)
    elif notas > 10 :
        print("valor invalido")
    else: 
        i += 1
materias_reprobadas =", ".join(materias)
print('El alumno debe recursar las materias: {}'.format(materias_reprobadas))