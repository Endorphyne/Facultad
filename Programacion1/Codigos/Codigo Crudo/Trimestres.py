def trimestre1():
    t1 =[]
    i = 0
    while i != 3 :
        dato = input("Ingrese la nota Nº({}) del PRIMER trimestre, si no desea ingresar nota presione ENTER: ".format(i+1))
        if dato == '':
            for x in range(3):
                t1.append(0)
                i = 3
        elif dato != '$' and i != 3:
            nota = float(dato)
            if nota < 0 and nota > 10 :
                while nota < 1 and nota > 10:
                    nota = input('Valor invalido, vuelva a ingresar la nota o comando de salida.')
            elif nota >= 1 and nota <= 10 :
                nota = dato  
            i += 1
            t1.append(float(nota))
    promedio1 = 0.0
    for x in t1 :
        promedio1 += x 
    promediofinalT1 = promedio1/3
    return t1, promediofinalT1
def trimestre2():
    t2 =[]
    i = 0
    while i != 3 :
        dato =input("Ingrese la nota Nº({}) del SEGUNDO trimestre, si no desea ingresar nota presione ENTER: ".format(i+1))
        if dato == '':
            for x in range(3):
                t2.append(0)
                i = 3
        elif dato != '$' and i != 3:
            nota = float(dato)
            if nota < 0 and nota > 10 :
                while nota < 1 and nota > 10:
                    nota = input('Valor invalido, vuelva a ingresar la nota o comando de salida.')
            elif nota >= 1 and nota <= 10 :
                nota = dato  
            i += 1
            t2.append(float(nota))
    promedio2 = 0.0
    for x in t2 :
        promedio2 += x 
    promediofinalT2 =promedio2//3
    return t2,promediofinalT2
def trimestre3():
    t3 =[]
    i = 0
    while i != 3 :
        dato =input("Ingrese la nota Nº({}) del TERCER trimestre, si no desea ingresar nota presione ENTER: ".format(i+1))
        if dato == '':
            for x in range(3):
                t3.append(0)
                i = 3
        elif dato != '$' and i != 3:
            nota = float(dato)
            if nota < 0 and nota > 10 :
                while nota < 1 and nota > 10:
                    nota = input('Valor invalido, vuelva a ingresar la nota o comando de salida.')
            elif nota >= 1 and nota <= 10 :
                nota = dato  
            i += 1
            t3.append(float(nota))
    promedio3 = 0.0
    for x in t3 :
        promedio3 += x 
    promediofinalT3 = promedio3/3
    print(t3)
    return t3, promediofinalT3
def anual(a,b,c):
    valores1 = a
    valores2 = b
    valores3 = c
    promedioAnual =(valores1+valores2+valores3)/3
    return promedioAnual
