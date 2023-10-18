#Biblioteca
#Escribi una funcion 
def menuExtra():
    while True:
        opcion2 = input("""
AJA! sorpresa, ahora tendras que elejir otra opcion ingresa 1/2/3 (0 para volver al menu anterior)
                       -Opcion (1)
                       -Opcion (2)
                       -Opcion (3)
                       -Salir (0)""")
        if opcion2 == '1' :
            print("give")
        elif opcion2 == '2' : 
           print('You')
        elif opcion2 == '3':
            print("up")
        elif opcion2 == '0':
            break
        else :
            print("Valor Invalido")
