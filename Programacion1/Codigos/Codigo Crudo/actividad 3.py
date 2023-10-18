"""Crear una lista, agregar nums de 1 a 10 a la lista, recorrer la lista en orden inverso e imprimir los numeros separados por coma"""
numeros = []
for x in range(1, 11):
    numeros.append(x)
print(*reversed(numeros))