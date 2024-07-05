import numpy
vector = []
def suma(vector):
    return numpy.sum(vector)
def producto(vector):
    return numpy.prod(vector)
def max_Min(vector):
    out =[]#lista donde el primer valor es el mininmo y el segundo el maximo
    out.append(numpy.min(vector))
    out.append(numpy.max(vector))
    return out
def media_Aritmetica(vector):
    return numpy.mean(vector)
    
for x in range(int(input("Ingrese la cantidad de elementos del vector: "))):
    vector.append(float(input(f"Ingrese el elemento ({x+1}) del vector: ")))

print(f"""
Suma de los elementos: {suma(vector)}
Producto de los elementos: {producto(vector)}
Valor Maximo: {max_Min(vector)[1]}
Valor Minimo: {max_Min(vector)[0]}
Media Aritmetica: {media_Aritmetica(vector)}""")