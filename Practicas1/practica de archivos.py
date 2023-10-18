archivo = open("Practicas 1\practica de archivos.txt", "a")
ingreso = str(input("Ingrese una palabra/s de al menos 3 caracteres de longitud:\n "))
ingreso += "\n"
while len(ingreso) < 3 :
    ingreso = str(input("La/s palabra/s deben ser de al menos 3 caracteres de longitud:\n "))
    ingreso += "\n"
archivo.write(ingreso)
archivo.close()