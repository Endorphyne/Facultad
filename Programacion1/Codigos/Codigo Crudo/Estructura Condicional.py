print('Ingrese la nota')
nota = float(input())
if nota==10 :
    print('Excelente')
elif nota == 9 :
    print('sobresaliente')
elif nota < 9 and nota > 6 :
    print('Muy Bueno')
elif nota == 6 :
    print('Bueno')
elif nota <= 5 :
    print('Regular')
elif nota <= 3 :
    print('Anda ahorrando para comprar un remis')
else :
    print('Valor no valido')