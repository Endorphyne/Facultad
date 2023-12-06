import random
def adivinarPais():
    lista_paises = [['Argentina','America del Sur','Español','Actual campeon de la copa mundial de futbol'],['Egipto','Africa','Arabe','Cuna de la civilizacion mas antigua del mundo'],['Arabia','Asia','Arabe','Cuenta con dos de las ciudades mas importantes para el Islam'],['España','Europa','Español','Una de las pocas monarquias existentes en el mundo'],['Australia','Oceania','Ingles','Famosa por su flora y fauna endemicas y megadiversas']]
    pais_elegido = lista_paises[random.randrange(0,len(lista_paises))]
    intentos = 2
    pista =[]
    while intentos > 0 and intentos != 5:
        while len(pista) < 2:
            try:
                usuario = input("Seleccione que pistas va a desear\n 1: Continente\n 2: Idioma\n 3: Curiosidad\n =")
                usuario = int(usuario)
                usuario in pista == False
            except:
                print("Opcion ingresada invalida")
            else:
                if usuario not in pista:
                    pista.append(usuario)
        for x in pista:
            print(f"La pistas son: {pais_elegido[x]}")
        try:
            intento_Usuario = input("Ingrese el Pais a intentar\n =")
            intento_Usuario = intento_Usuario.upper()
        except:
            print("Valor ingresado invalido")
        else:
            if intento_Usuario == pais_elegido[0].upper():
                print(f"FELICIDADES!!! haz adivinado el pais {pais_elegido[0]}")
                intentos = 5
            else:
                intentos -= 1
                if intentos != 0:
                    print(f"Animo, aun te quedan {intentos} intentos")
                elif intentos == 0:
                    print(f"Que lastima haz perdido, el pais a adivinar era {pais_elegido[0]}")
# horas_trabajo = {
#     "domingo":0,
#     "lunes":5,
#     "martes":10,
#     "miercoles":8,
#     "jueves":8
# }
# print(horas_trabajo['martes'])
# if horas_trabajo["domingo"] > 0:
#     print("El domingo se trabajo")
# else:
#     print("El domingo no se trabajo")
# horas_trabajo['lunes'] = 7
# horas_trabajo.update({"Viernes":7})
# for x,y in horas_trabajo.items():
#     print(f"El dia {x} se trabajaron {y} horas")
adivinarPais()