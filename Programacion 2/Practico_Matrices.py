import numpy as vector
matriz1 =vector.array([[1,2,3],[4,5,6]])
matriz2 =vector.array([[7,8],[9,10],[11,12]])
try:
    opcion = int(input("Escoja la opcion a realizar \n1)SUMA\n2)Resta\n3Producto\n4)Division\n5)Ver valor de la matriz \n:"))
except:
    print("Valor invalido")
try:
    m1_Posicion1 = int(input("Ingrese la posicion de la matriz 1 que desee como primer valor:\n"))
    m1_Posicion2 = int(input())
    m2_Posicion1 = int(input("Ingrese la posicion de la matriz 2 que desee como segundo valor:\n"))
    m2_Posicion2 = int(input())
    resultado = "pepe"
    if opcion == 1:
        resultado = matriz1[m1_Posicion1][m1_Posicion2]+matriz2[m2_Posicion1][m2_Posicion2]
    elif opcion == 2:
        resultado = matriz1[m1_Posicion1][m1_Posicion2]-matriz2[m2_Posicion1][m2_Posicion2]
    elif opcion == 3:
        resultado = matriz1[m1_Posicion1][m1_Posicion2]*matriz2[m2_Posicion1][m2_Posicion2]
    elif opcion ==4:
        resultado = matriz1[m1_Posicion1][m1_Posicion2]/matriz2[m2_Posicion1][m2_Posicion2]
    else:
        print(f"La matriz 1 tiene el valor: {matriz1[m1_Posicion1][m1_Posicion2]} \nLa matriz 2 tiene el valor: {matriz2[m2_Posicion1][m2_Posicion2]} \nEn las posiciones solicitadas")
    if resultado != "pepe":
        print(f"El resultado de la operacion solicitada es: {resultado}")
except IndexError:
    print("Posicion de la matriz invalida")
except:
    print("Valor erroneo")