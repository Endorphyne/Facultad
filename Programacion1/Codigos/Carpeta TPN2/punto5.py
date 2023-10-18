print('Ingrese 2 valores')
n1 = int(input())
n2 = int(input())
if n1 == n2 : 
    print('Que no sean el mismo')
elif n1 > n2 :
    for x in range(n2, n1+1) : 
        if (x%2) == 0 :
            print(x, 'es par')
        else : 
            print(x, 'es impar')
elif n2 > n1 : 
    for x in range(n1, n2+1) : 
        if (x%2) == 0 :
            print(x, 'es par')
        else : 
            print(x, 'es impar')