nombres = ["Juan","Enrique","Alberto","Manolo","Pepe","Roberto","Borja"]
def listaSiNo():
    nombres_minuscula = []
    for x in nombres:
        nombres_minuscula.append(x.lower())
    while True:
        nombre = str(input("Ingrese un nombre para ver si esta en la lista, para salir ingrese (SALIR)"))
        nombreDefault = nombre
        nombre = nombre.lower()
        if nombre == "salir":
            break
        if nombre in nombres_minuscula :
            print("El nombre esta en la lista")
        else:
            nombres.append(nombreDefault)
            nombres_minuscula.append(nombre)
            print("El nombre no esta en la lista")
listaSiNo()