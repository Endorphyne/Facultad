import random
def contadorCaraceteres(cadena):
    caracteres = {}
    for x in cadena:
        if x not in caracteres:
            caracteres[x] = 1 
        else:
            caracteres[x] += 1 
    return caracteres
def numeroDNI(DNI):
    DNI = str(DNI)
    check = 0
    for x in DNI: 
        if x == [0-9] :
            check += 1
    return check >= 7 & check <= 8
def titulo(cadena):
    return cadena.title()
def email(correo):
    return "@" in correo 
def primo(numero):
    return numero % numero == 0 and numero % 2 != 0 
def adivinador(): 
    numero = random.randrange(1,100)
    intentos = 0 
    while intentos < 5 :
        attempt = int(input("Ingrese un numero para intentar"))
        if attempt > numero :
            intentos +=1 
            print("Prueba ingresando un numero menor")
            print(f"LLevas: {intentos} intentos")
        elif attempt < numero:
            intentos += 1 
            print("Prueba ingresando un numero mayor")
            print(f"LLevas: {intentos} intentos")
        elif attempt == numero:
            print(f"""Felicidades
                  Has adivinado el numero {numero}
                  con tan solo {intentos} intentos""")
    print(f"No has logrado adivinar el numero: {numero}")
def adivinador_pistas():
    numero = random.randrange(1,100)
    intentos = 0 
    pistas = 2
    attempt = 0 
    while intentos < 5 :
        attempt = int(input("""Ingrese un numero para intentar, si deseas una pista ingresa el numero : 314
                            : """))
        if attempt > numero and attempt != 314 :
            intentos +=1 
            print("Prueba ingresando un numero menor")
            print(f"LLevas: {intentos} intentos")
        elif attempt < numero:
            intentos += 1 
            print("Prueba ingresando un numero mayor")
            print(f"LLevas: {intentos} intentos")
        elif attempt == numero:
            print(f"""Felicidades
                  Has adivinado el numero {numero}
                  con tan solo {intentos} intentos""")
        elif attempt == 314 and pistas > 0:
            pista = int(input("""Ingrese que pista desea obtener:
                              1 - Saber si es par o impar 
                              2 - Indicar si se encuentra entre 1-50 o 51-100 
                              3 - Indicar si el ultimo numero ingresado comparte alguna cifra con el numero a adivinar"""))
            if pista == 1 : 
                if numero % 2 == 0 :
                    print("El numero a adivinar es par")
                else: 
                    print("El numero a adivinar es impar")
                pistas -=1 
            elif pista == 2 :
                if numero >= 51 and numero <= 100 :
                    print("El numero se encuentra enter 51 y 100")
                else : 
                    print("El numero se encuentra entre 1 y 50")
                pistas -= 1
            elif pista == 3 : 
                if attempt == 314 :
                    attempt = int(input("Ingrese un numero para intentar usar esta pista"))
                numerino = str(numero)
                numerino2 = str(attempt)
                for x in numerino2 : 
                    if x in numerino:
                        print(f"El numero en comun es el {x}")
                    elif x not in numerino:
                        print(f"El numero {x} no se encuentra en el numero")
                pistas -= 1
    print(f"No has logrado adivinar el numero: {numero}")