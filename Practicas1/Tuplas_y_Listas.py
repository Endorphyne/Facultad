#UNIDAD 4 LISTAS Y TUPLAS
#syntaxis:
#   lista = [x, y, z]
#syntaxis Listas anidadas:
#   listaAnidada = [1, [2, 3], 4]
#=====================================
#METODOS DE LISTAS
#lista.append() //util para construir una lista agregando los elementos al final de la misma 
#lista.insert()//util para insertar un item en una lista con una index en concreta
#lista.count()//util para buscar la cantidad de X objetos en una lista
#lista.index()//Devuelve el indice de X item en una lista
#lista.remove()//Elimina un valor X de una lista
#Palabra reservada "in" // sirve para una decisio booleana en una lista print("x" in lista)
#for x in lista // itera la lista almacenando el valor que itera en cada vuelta en x
#len() //nos sirve para ver la longitud de una cadena
#lista.pop()// elimina un item en X indice
#del lista[0] // elimina lo que este en la lista basado en un indice, rango o la lista entera
#===================================================================================================
#TUPLAS
#funcionan similar a las listas en python
#son identificadas por la sintaxis con parentesis () en lugar de corchetes []
#syntaxis:
#   tupla = ()
#===================================================================================
#EJERCICIOS
# ===============================================================================
#1)
# listaAumentada =[]
# for x in range(10):
#     listaAumentada.append(x)
# print(listaAumentada)
# ==============================================================
#2)
listaNatural = []
exponencial = 1
for o in range(10):
    i = 0
    exponencial = exponencial*2
    aux =[]
    for x in range(exponencial):
        i+=1
        aux.append(i)
    listaNatural.append(aux)
print(listaNatural)
#=========================================================================
#3)
# listaAbecedario = ['a','b','c','d','e','f','g']
# print(listaAbecedario)
# listaAbecedario[2] = 'x'
# if 'j' in listaAbecedario :
#     pass