biblioteca = {}
salida = 'z'
while salida != 'x' :
    salida = str(input('''
        BIBLIOTECA
        -----------------
        1 - Buscar un libro
        2 - Agregar un libro 
        x - salir 
        Ingrese una opción (1-2/x): '''))
    if salida == '1' :
        eleccion = input('Introduce el libro a buscar: ')
        if  eleccion in biblioteca:
            print('''
        Libro: {libro}
        Autor: {autor}
        presione ENTER para continuar'''.format(libro=eleccion,autor=biblioteca[eleccion]))
            espera = input()
            print(biblioteca[libro])
            print(biblioteca)
        else :
            print('''Libro no encontrado
                  Presione ENTER para continuar''')
            espera = input()
    elif salida == "2":
        libro = input('introduce el titulo del libro: ')
        if libro in biblioteca:
            print('''El libro YA esta ingresado
                  Presione ENTER para continuar''')
            espera = input()
        else :
            autor = input('introduce Apellido (y nombre/s) del autor: ')
            autor = autor.upper()
            print('''Añadido el contacto
                 Presione ENTER para continuar''')
            biblioteca[libro] = autor #agregado 10/08/23
            espera =  input()
    elif salida == 'x' : 
        print(biblioteca)
