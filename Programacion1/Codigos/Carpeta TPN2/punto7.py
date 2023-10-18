limite = int(input('Ingrese cantidad de numeros a introduccir: '))
print('introduzca los numeros hasta el limte')
n1 = int(input()) 
n3 = n1
for x in range(limite) : 
    n1 = int(input()) 
    if n3 > n1 : 
        print('El numero {n1} es menor que {n2} '.format(n1=n1,n2=n3)) 