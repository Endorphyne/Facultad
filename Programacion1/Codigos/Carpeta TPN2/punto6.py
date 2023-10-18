n1 = int(input('ingrese 1 numero para calcular sus divisores: '))
divisores = [n1,]
for x in range(1, (n1//2)+1) : 
    if (n1%(x)) == 0 : 
        divisores.append(x)
print('los divisores de {} son:'.format(n1),*sorted(divisores))