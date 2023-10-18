numeros = []
for i in range(int(input("Ingrese la cantidad de números a introducir: "))):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    if i > 0 and numero <= numeros[i-1]:
        print("El número {numeroMenor} no es mayor que el número {numeroAnterior}.".format(numeroMenor=numero, numeroAnterior=numeros[i-1]))