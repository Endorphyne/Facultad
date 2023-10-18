import Trimestres
lista_alumnos = {
    '12345678':['Dominguez','Juan',],
    '23456789':['Manolo','Roberto',],
}
def ingresarValores() :
    usuario = str(input('Ingrese su DNI para ingresar sus notas: '))
    if usuario in lista_alumnos:
        tri1=Trimestres.trimestre1()
        tri2=Trimestres.trimestre2()
        tri3=Trimestres.trimestre3()
        lista_alumnos[usuario].append('''Primer Trimestre:
         notas: {notas}
         Promedio: {promedio}'''.format(notas=tri1[0],promedio=tri1[1]))
        lista_alumnos[usuario].append('''Segundo Trimestre:
         notas: {notas}
         Promedio: {promedio}'''.format(notas=tri2[0],promedio=tri2[1]))
        lista_alumnos[usuario].append('''Tercer Trimestre:
         notas: {notas}
         Promedio: {promedio}'''.format(notas=tri3[0],promedio=tri3[1]))
        lista_alumnos[usuario].append(Trimestres.anual(tri1[1],tri2[1],tri3[1]))
        print('''DNI: {dni}
        Las notas del alumno {apellido} {nombre} son:
        Primer Trimestre: {t1}
        Segundo Trimestre: {t2}
        Tercer Trimestre: {t3}
        Promedio anual: {anual}'''.format(dni=[usuario],apellido=lista_alumnos[usuario][0],nombre=lista_alumnos[usuario][1],t1=lista_alumnos[usuario][2],t2=lista_alumnos[usuario][3],t3=lista_alumnos[usuario][4],anual=lista_alumnos[usuario][-1]))
    else:
      print('No se encuentra en el sistema.')
    return lista_alumnos
ingresarValores()