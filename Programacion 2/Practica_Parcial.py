def procesar_Cadena(cadena=""):
    return cadena.strip().lower().replace("a","@")
# print(procesar_Cadena(""))

def contar_palabras(lista=[]):
    dict_Lista = {}
    for x in range(len(lista)):
        if lista[x] in dict_Lista:
            dict_Lista[f'{lista[x]}'] += 1
        else:
            dict_Lista.update({f"{lista[x]}":1})
    return dict_Lista
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo","Lunes"]

# print(contar_palabras(dias_semana))

def vectores():
    vec1 =[]
    vec2 =[]
    for x in range(2):
        for i in range(5):
            try:
                data = int(input(f"Introduzca el valor N({i+1}) del vector N({x+1})"))
            except:
                print("tipo de dato erroneo")
            if x+1 == 1:
                vec1.append(data)
            else:
                vec2.append(data)
    lista=[]
    for x in range(5):
        lista.append(vec1[x]+vec2[x])
    return lista

# print(vectores())

def matrices(m1,m2):
    suma = [[],[]]
    if len(m1) != len(m2):
        return None
    else:
        for x in range(len(m1)):
            for i in range(len(m1[x])):
                if x == len(m1)/2:
                    suma[0].append(m1[x][i] + m2[x][i])
                else:
                    suma[1].append(m1[x][i] + m2[x][i])
    return suma
# print(matrices([[1,2,3],[3,2,1]],[[5,4,3],[5,4,3]]))
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito exitoso. El saldo actual es de {self.saldo}.")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retiro exitoso. El saldo actual es de {self.saldo}.")
        else:
            print("No hay suficiente saldo para realizar el retiro.")

    def mostrar_saldo(self):
        print(f"El saldo actual es de {self.saldo}.")
