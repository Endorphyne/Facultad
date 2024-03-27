# Crear una funcion que lea una cadena de caracteres y cuente cada una de las vocales y la cantidad de las mismas
# def contadorVocales():
#     vocales = ("a","e","i","o","u")
#     cantidadVocales= 0
#     texto = str(input("Ingrese una cadena para contar sus vocales: "))
#     for x in texto:
#         if x.lower() in vocales:
#             cantidadVocales += 1
#     return cantidadVocales
# print(contadorVocales())

#Crear una funcion que actualice el salario de los empleados tomando como valores un diccionario de empleados(empleado:sueldo) y que le suba el salario en un 30% 
def aumentarSueldos(empleados,aumento = 0.3):
    for x,y in empleados.items():
        incremento = y * aumento
        y += incremento
        empleados.update({x:y})
empleados = {
    "jhonny":200_000, 
    "bravo":100_000,
    "Juana":300_000
}
aumentarSueldos(empleados)
print(empleados)