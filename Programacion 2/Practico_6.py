# En una planta se hacen relevamientos de fallas ocurridas durante cada semana de un mes. 
# Se registran las fallas para los distintos sectores en la planta, identificadas por su nombre. Para cada sector se registran las fallas que surgen durante cada semana del mes. 
# Para registrar se necesitará ingresar el nombre del sector, la semana a la que corresponda la falla y la cantidad de fallas ocurridas. Si se ingresa una falla para un sector/semana que ya posea registro, se agregará la última a lo existente. 
# Las fallas para cada semana se registrarán en una lista, y la misma estará asociada a un elemento del diccionario. El diccionario se llamará fallos. 
# La clave para el diccionario será el nombre del sector en la planta. 
from os import system as sm
from time import sleep as amomir
import numpy as vector
fallos = {}
fallos_Prueba={
    "comercio":vector.array([0,3,4,5]),
    "fabrica":vector.array([1,4,5,0]),
    "poposio":vector.array([0,0,0,1])
}
def cleanex():
    amomir(1)
    sm("cls")
    amomir(1)
#funcion encargada de registrar los fallos recibe el diccionario vacio o con datos
def registrar_Fallas(diccionario):
    try:
        #ingreso de datos para el diccionario
        sector = str(input("Ingrese el sector en el que ocurrio la falla: "))
        len(sector)>0#verifica que el sector no este vacio
        semana = int(input("Ingrese la semana en la que ocurrio el fallo: "))-1
        semana <= 4 and semana >=0
        cantidad_Fallos = int(input("Ingrese la cantidad de fallos que hubieron: "))
        #verifica si el sector mencionado esta en el diccionario o no
        if sector in diccionario:
            #suma de la cantidad de datos al diccionario
            diccionario[sector][semana]+=cantidad_Fallos
        else:
            #agrega el sector al diccionario, ademas de cargar una semana vacia y sumar la cantidad de fallos a la correspondiente
            diccionario.update({f"{sector}":vector.array([0,0,0,0])})
            diccionario[sector][semana] += cantidad_Fallos
    except:
        #mensaje de error de datos
        print("Valor Invalido")
        cleanex()
def sector_Mayores_Fallas(diccionario):
    valor_Max = 0
    for x,y in diccionario.items():
        if vector.sum(y)>valor_Max:
            valor_Max = vector.sum(y)
            sector_Max = x
    print(f"El sector con mas fallas en el mes fue: {sector_Max} con {valor_Max} fallas")
    amomir(1)
def promedio_Fallas(diccionario):
    print("Bienvenido al sector de promedio de fallas")
    suma=0
    cantidad=0
    try:
        semana = int(input("Ingrese la semana que desea sacar promedio: "))-1
        semana<4 and semana >0
    except:
        cleanex()
        print("Valor invalido")
    for x in diccionario.values():
        cantidad +=1
        suma += x[semana]
    print(f"El promedio de la semana {semana} es de {suma/cantidad}")
def sector_Mayores_Semana(diccionario):
    sectores_con_mas_fallas = []
    num_semanas = len(diccionario[next(iter(diccionario.keys()))])  # número de semanas
    for semana in range(num_semanas):
        fallas_semana = {sector: fallas[semana] for sector, fallas in diccionario.items()}
        sector_mayor_fallas = max(fallas_semana, key=fallas_semana.get)
        sectores_con_mas_fallas.append(sector_mayor_fallas)
    
    for x in range(len(sectores_con_mas_fallas)):
        print(f"El sector con mas fallas en la semana ({x}) fue: ({sectores_con_mas_fallas[x]})")

def dic_MayorN_FallasSec(diccionario):
    mayor_Falla_Por_Sector = {}
    for sector,fallas in diccionario.items():
        mayor_Falla_Por_Sector[sector] = vector.max(fallas)
    for sector,fallas in mayor_Falla_Por_Sector.items():
        print(f"El sector {sector} tuvo ({fallas} fallas)")
def mostrar_Menu(opcion=0):
    while opcion != "9":
        cleanex()
        opcion=str(input("Ingrese la opcion que desea realizar: \n1)Registrar una falla\n2)Sector con mayor cantidad de fallas en el mes\n3)Promedio de fallas de una semana solicitada\n4)Sector que presento mayor numero de fallas por cada semana\n5)Semana que presenta mayor numero de fallas para cada sector\n9)Salir\nOpcion: "))
        if opcion == "1":
            registrar_Fallas(fallos_Prueba)
        elif opcion=="2":
            sector_Mayores_Fallas(fallos_Prueba)
        elif opcion=="3":
            promedio_Fallas(fallos_Prueba)
        elif opcion =="4":
            sector_Mayores_Semana(fallos_Prueba)
        elif opcion == "5":
            dic_MayorN_FallasSec(fallos_Prueba)
        elif opcion == "9":
            continue
        else:
            print("Valor Invalido")
            cleanex()
mostrar_Menu()