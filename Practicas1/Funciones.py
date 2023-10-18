import os
#FUNCIONES
#syntaxis de la funcion
#def NombreFuncion(Parametros):
#   Cuerpo
#===========================================================================================
# variable = 1
# def multiplicarX2(a):
#     return(a*2)
# def sumar(N1,N2):
#     return(N1+N2)
# print(sumar(sumar(1,2),sumar(4,1)))
#===========================================================================================
# def imprimir_lista_nombres(nombres):
#     for x in nombres:
#         print(x)
# nombres = ["juan","alberso","ricardo","manuela"]
# imprimir_lista_nombres(nombres)
# def es_par(numero):
#     condicion = False
#     if numero % 2 == 0 :
#         condicion = True
#     return condicion
#     # return numero % 2 == 0
#===========================================================================================
# def funcion_anon(dic,nombre):
#     return nombre in dic.keys()
# edades_personas = {
#     "juan"  : 20,
#     "delia" : 15,
#     "julia" : 45
# }
# print(funcion_anon(edades_personas,"juan"))
# print(funcion_anon(edades_personas,"juana"))
#===========================================================================================   
#Declara parametros opcionales
#
# def pedir_confirmacion(prompt,reintentos=3,queja='Si o no por favor'):
#     while True:
#         if reintentos <= 0:
#             print('Sos Paola Argento')
#         ok = input(prompt).lower()
#         ok = ok[0]
#         if ok == "s":
#             return True
#         elif ok == 'n':
#             return False
#         else:
#             os.system('cls')
#             print(queja)
#             reintentos -= 1
# print(pedir_confirmacion("Desea crear el archivo? "))
##===========================================================================================
# def edades(edad,mayoria_edad=18):
#     return edad >= mayoria_edad
# print(edades(22))