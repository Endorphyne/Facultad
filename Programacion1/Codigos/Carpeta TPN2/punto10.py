numeros_pares = 0
numeros_impares = 0 
for x in range(int(input('Ingrese la cantidad de numeros introducir: '))):
    numero  = int(input('Ingrese los numeros: '))
    if (numero%2) == 0 :
        numeros_pares += 1 
    else :
        numeros_impares += 1 
print('hubieron {impares} numeros impares y {pares} numeros pares'. format(impares = numeros_impares, pares = numeros_pares))