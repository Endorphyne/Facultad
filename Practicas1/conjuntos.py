# DICCIONARIOS
# los conjuntos son declarados con {}
empresas = {'ibm','dell','ibm','amd','intel'}
# cuando queremos evitar repetidos usar los conjuntos es la practica correcta, porque los conjuntos no admiten repetidos
# los valores NO estan ordenados
# se pueden realizar comprobaciones como si fueran listas 
# tambien se pueden utilizar las estructuras repetitivas 
# empresas.add('HP') sirve para añadir un nuevo item al conjunto
# empresas.update('lenovo','razor') sirve para añadir de forma grupal items al conjunto
# la mayoria de funciones son utilizables con los conjuntos (ej:len)
# empresas.discard('dell') se utiliza para remover un item del conjunto
# empresas.clear() se tuiliza para limpiar todo el conjunto 
# se puede usar el metodo set() para crear un conjunto
# 
a = set("abracadabra")
b = set("alakazam")
# Algunos metodos para comparar conjuntos
# 1) DIFERNCIA = '-' devuelve los items que estan en a pero no en b "print(a-b)"
# difference()= METODO ASOCIADO aplicado al primer conjunto que recibe como parametro el segundo conjunto ="print(a.difference(b))"
# 2)Interseccion ='&' toma los items de ambos conjuntos y los imprime, evitando repetidos 'print(a&b)
# intersection() METODO ASOCIADO
# 3)Union = '|'imprime solo los items que esten en ambos conjuntos "print(a|b)"
# union() METODO ASOCIADO
# 4)diferencia simetrica = '^' imprime solamente lo que este en uno o en el otro pero no lo que este en ambos 
# symmetric_difference() METODO ASOCIADO