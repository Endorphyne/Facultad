print('introduzca los numeros hasta el limte')
numeros_negativos = 0
for x in range(int(input('Ingrese cantidad de numeros a introduccir: '))) : 
    n1 = int(input()) 
    if n1 < 0 : 
        numeros_negativos += 1
print('La cantidad de numeros negativos es {}'.format(numeros_negativos))