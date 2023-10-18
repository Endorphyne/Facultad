import random 
archivo = open("wordle.txt", "r")
palabras =[]
for x in archivo:
    palabras.append(x.rstrip())
palabraElegida = palabras[random.randint(0,len(palabras))]
intentos = 0 
victoria = False
while True :
    attempt = str(input("Ingrese una palabra para intentar adivinar: \n"))
    while len(attempt) != 5 : 
        attempt = str(input("El largo de la palabra es invalido ingreselo de nuevo: \n")) 
    intentos += 1
    if attempt == palabraElegida:
        print(f"Haz ganado, la palabra era: {palabraElegida} con tan solo: {intentos} intentos")
        victoria = True
        break
    if intentos == 7: 
        break
    if intentos != 7 :
        for x in range(len(attempt)):
            if attempt[x] == palabraElegida[x] :
                print(f"La letra ({attempt[x]}) se encuentra en la posicion {x+1} de la palbra")
            elif attempt[x] in palabraElegida:
                print(f"La letra {attempt[x]} esta en la palabra, pero en otra posicion")
            elif attempt[x] not in palabraElegida:
                print(f"La letra {attempt[x]} no se encuentra en la palabra")
if victoria == False : 
    print(f"Se termino el juego, la palabra era {palabraElegida}")