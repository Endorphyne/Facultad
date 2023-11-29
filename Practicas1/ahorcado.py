import random
from etapas_ahorcado import etapas
dificultad = str(input("""Seleccione que dificultad desea usar:
                       1 = Facil
                       2 = Normal
                       3 = Dificil
                       :"""))
archivo = open("ahorcado.txt", 'r')
victoria = False
palabra = ""
gui_intento=[]
letras =[]
vidas = 0
palabras =[]
if dificultad == '1':
    vidas = 7
    etapa = 0
    for x in archivo:
        x = x.rstrip()
        x = x.split("_")
        for i in x:
            i = i.lower()
            if len(i) <= 8:
                palabras.append(i)
elif dificultad == "2":
    vidas = 6
    etapa = 1
    for x in archivo:
        x = x.rstrip()
        x = x.split("_")
        for i in x:
            i = i.lower()
            if len(i) <= 15 or len(i) >= 9:
                palabras.append(i)
elif dificultad == "3":
    vidas = 5
    etapa = 2 
    for x in archivo:
        x = x.rstrip()
        x = x.split("_")
        for i in x:
            i = i.lower()
            if len(i) > 15 :
                palabras.append(i)
palabra = palabras[random.randrange(0,len(palabras))]
for x in palabra:
    o = 0
    if x != " ":
        gui_intento.append("_")
    o += 1
    if x == " ":
        gui_intento.append(" ")
while vidas > 0 and victoria == False:
    print(etapas[etapa])
    for x in gui_intento:
        print(x,end="")
    intento = str(input("\nIngrese una letra: "))
    if len(intento) > 1 or len(intento) < 1:
        intento = str(input("INGRESAR SOLAMENTE UNA LETRA"))
    for x in range(len(palabra)):
        if intento in palabra[x]:
            gui_intento[x] = intento
        else :
            if intento not in letras:
                letras.append(intento)
    print(f"Letras usadas {letras}")
    if "".join(gui_intento) == palabra.lower():
        victoria = True
    if intento not in palabra:
        vidas -= 1
        etapa += 1
if victoria == True:
    print(f"Felicidades Ganaste la palabra era {palabra}")
else:
    print(f"Haz fallado la palabra era {palabra}")    