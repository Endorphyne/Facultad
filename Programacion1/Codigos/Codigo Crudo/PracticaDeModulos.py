#Realizar un menu con varias opciones con funciones en una biblioteca
from PracticaDeModulos2 import menuExtra
def menuPrincipal():
    while True:
        opcion = input("""
    Elija una opcion para averiguar que hace ingresando 1/2/3 (0 para salir):
        -Opcion (1)
        -Opcion (2)
        -Opcion (3)
        -Salir (0)""")
        if opcion == '1':
            print('Never')
        elif opcion == '2':
            print("gonna")
        elif opcion == '3' :
            menuExtra()
        elif opcion == '0':
            break
        else: 
            print('Valor Invalido')
menuPrincipal()