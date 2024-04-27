#Programa libreria
libreria = {
    "IBN203" : ["Pepito el grillo", "Pepa", 789],
    "IBN100" : ["La velada","Jhordy Jhannos", 1]
}
bandera = True
while bandera:
    try:
        var_busqueda = input("Ingrese el IBN del libro que desea ingresar: ").upper()
        if var_busqueda in libreria:
            print(f"""
Titulo: {libreria[var_busqueda][0]}
Autor: {libreria[var_busqueda][1]}
Numero de Paginas: {libreria[var_busqueda][2]}""")
        else:
            print("El libro no se encuentra")
        salida = input("Desea buscar otro libro? (Si/No)").upper()
        if salida == "NO" or salida == "N":
            bandera = False
    except:
        print("De alguna forma metiste un valor invalido, felicidades")