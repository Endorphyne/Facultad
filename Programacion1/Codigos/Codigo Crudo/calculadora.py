print('''Ingrese valor de operacion a seleccionar
1)SUMA
2)RESTA
3)MULTIPLICACION
4)DIVISION
''')

operacion = int(input())

if operacion == 1:
    resultado = 0
    print("Ingrese valores a sumar, cuando termine de sumar escriba EXIT")
    cantidadValores = 0

    while True:
        valores = input()
        if valores == "EXIT":
            break 
        resultado += float(valores)
    
    print("La suma es:", resultado)
if operacion == 2 :
    print("Ingrese valor inicial:")
    valores=input()
    resultado=0
    print("ingrese valores para restar, cuando acabe escriba EXIT")
    cantidadValores =0 
    while True:
        valores=input()
      #  print(valores,"-")
        if valores == "EXIT" :
            break
        resultado -= float(valores)
    print("El resultado es:", resultado)
if operacion == 3 :
    resultado = 0 
    print("Ingrese valores a multiplicar, cuando acabe escriba EXIT")
    cantidadValores=0
    while True:
        valores=input()
        if valores == "EXIT" :
            break
        resultado *= float(valores)
    print