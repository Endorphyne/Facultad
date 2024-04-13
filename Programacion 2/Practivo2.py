from os import system as clear
from math import sqrt
bandera = True
while bandera:
    try:
        op = int(input("Ingrese que operacion desea realizar: \n 1) Suma \n 2) Resta \n 3) Multiplicacion \n 4) Division \n 5) Potencia \n 6)Raiz cuadrada \n 7) SALIR: "))
        op >= 1 and op <= 7
        if op == 7:
            break
    except:
        clear("cls")
        print("valor ingresado invalido")
    else:
        try:
            n1 = float(input("Ingrese el primer numero: "))
            if op != 6:
                n2 = float(input("Ingrese el segundo numero: "))
                if op == 4 and n2 == 0:
                    raise ValueError("No se puede dividir por 0")
        except ValueError as e: 
            clear("cls")
            print(f"Error:{e} o valor ingresado invalido")
        else:
           if op == 1:       
               print(f"El resultado es {n1 + n2}")
           elif op == 2:
               print(f"El resultado es {n1 - n2}")
           elif op == 3:
               print(f"El resultado es {n1 * n2}")
           elif op == 4:
               print(f"El resultado es {n1/n2 }")
           elif op == 5:
               print(f"El resultado es {n1**n2}")
           elif op == 6:    
               print(f"El resultado es {sqrt(n1)}")