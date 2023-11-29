blue = open("blue.txt","r")
mep = open("mep.txt","r")
valoresBlue =[]
valoresMep =[]
for x in blue:#bucles para obtener los valores de los archivos
    valoresBlue.append(x.rstrip())
for y in mep:
    valoresMep.append(y.rstrip())
ValoresA =[]
ValoresB =[]
for x in valoresBlue:
    A = x.split("-")
    ValoresA.append(A)
for y in valoresMep:
    B = y.split('-')
    ValoresB.append(B)
eleccion = str(input("Seleccione que opcion desea realizar:\n 1:Convertir\n 2:Consulta Cotizacion\n 3:Salir\n = "))
while eleccion != "3":
    if eleccion == "1":
        eleccion = str(input("Seleccione que desea realizar:\n 1:Pesos a Dolares\n 2:Dolares a pesos\n 3:Salir\n ="))
        if eleccion == "1":#primera opcion donde se realiza la division para la conversion (dependiendo de la opcion elegida)
            aux = False#valor bandera para el bicle de la linea 27 y 40
            cotizacion = str(input("Ingrese la cotizacion:\n BLUE\n MEP\n ="))
            if cotizacion.upper() == "BLUE":
                valor = ValoresA[-1][1]
                valor = float(valor)
                while aux == False:
                    try:
                        cantidad = input("Ingrese la cantidad de pesos a convertir\n =")
                        cantidad = float(cantidad) 
                        cantidad > 0 
                    except:
                        print("La cantidad ingresada es un valor invalido o negativo")
                    else:
                        aux = True
                        print(f"{cantidad} pesos son {cantidad/valor} dolares(BLUE)")
            elif cotizacion.upper() == "MEP":
                valor = ValoresB[-1][1]
                valor = float(valor)
                while aux == False:
                    try:
                        cantidad = input("Ingrese la cantidad de pesos a convertir\n =")
                        cantidad = float(cantidad) 
                        cantidad > 0 
                    except:
                        print("La cantidad ingresada es un valor invalido o negativo")
                    else:
                        aux = True
                        print(f"{cantidad} pesos son {cantidad/valor} dolares(MEP)")
            else:
                print("Valor invalido")
            eleccion = str(input("Seleccione que opcion desea realizar:\n 1:Convertir\n 2:Consulta Cotizacion\n 3:Salir\n = "))
        elif eleccion == "2":
            aux = False#valor bandera para el bicle de la linea 59 y 72
            cotizacion = str(input("Ingrese la cotizacion:\n BLUE\n MEP\n ="))
            if cotizacion.upper() == "BLUE":
                valor = ValoresA[-1][1]
                valor = float(valor)
                while aux == False:
                    try:
                        cantidad = input("Ingrese la cantidad de pesos a convertir\n =")
                        cantidad = float(cantidad) 
                        cantidad > 0 
                    except:
                        print("La cantidad ingresada es un valor invalido o negativo")
                    else:
                        aux = True
                        print(f"{cantidad} dolares son {cantidad*valor} pesos(BLUE)")
            elif cotizacion.upper() == "MEP":
                valor = ValoresB[-1][1]
                valor = float(valor)
                while aux == False:
                    try:
                        cantidad = input("Ingrese la cantidad de pesos a convertir\n =")
                        cantidad = float(cantidad) 
                        cantidad > 0 
                    except:
                        print("La cantidad ingresada es un valor invalido o negativo")
                    else:
                        aux = True
                        print(f"{cantidad} dolares son {cantidad*valor} pesos(MEP)")
            else:
                print("Valor invalido")
            eleccion = str(input("Seleccione que opcion desea realizar:\n 1:Convertir\n 2:Consulta Cotizacion\n 3:Salir\n = "))
    elif eleccion == "2":
            valor1_Blue = float(ValoresA[-1][1])#obtenciones de los 2 ultimos valores en los las listas
            valor2_Blue = float(ValoresA[-2][1])
            valor1_Mep = float(ValoresB[-1][1])
            valor2_Mep = float(ValoresB[-2][1])
            ele = str(input("Elija que cotizacion quiere consultar\n Mep\n Blue\n ="))
            if ele.upper() == "BLUE":
                cotizacion = round(((valor1_Blue*100)/valor2_Blue)-100,2)#formulas de cotizacion
            else:
                cotizacion = round(((valor1_Mep*100)/valor2_Mep)-100,2)
            if cotizacion < 0:#revisa si la cotizacion fue positiva o negativa
                simbolo = ""
            else:
                simbolo = "+"
            print(f"La cotizacion del dolar {ele.upper()} | {simbolo}{cotizacion}")
            eleccion = str(input("Seleccione que opcion desea realizar:\n 1:Convertir\n 2:Consulta Cotizacion\n 3:Salir\n = "))
    else:
        print("Eleccion invalida")
        eleccion = str(input("Seleccione que opcion desea realizar:\n 1:Convertir\n 2:Consulta Cotizacion\n 3:Salir\n = "))