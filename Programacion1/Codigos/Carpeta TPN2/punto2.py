print('Ingrese numeros para dividir')
n1 = int(input())
n2 = int(input())
if n2 == 0 or n1 == 0 : 
    print('valor invalido')
else :
    print('La division es', n1/n2)
    if (n1%n2) == 0 :
        print('La division es exacta')
    else: 
        print('La division no es exacta')