print('Ingrese el año actual')
año_actual = int(input())
print('Ingrese un año cualquiera')
año_random = int(input())
if (año_actual - año_random) == -1 :
    print(año_random, 'sera en 1 año')
elif (año_actual - año_random) == 1 :
    print(año_random, 'fue hace 1 año')
elif año_actual < año_random :
    print('Faltan', año_random - año_actual, 'años para el',año_random)
else :
    print('El', año_random, 'fue hace', año_actual - año_random, 'años')