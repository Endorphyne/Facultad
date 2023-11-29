def ingresar_gastos():
    archivo = open("GUI_Horodeski_Lautaro\Enero.txt","r+")
    archivo_de_gastos = open("GUI_Horodeski_Lautaro\gastos.txt","w")
    gastos = []
    for x in archivo:
        gastos.append(int(x.rstrip()))
    dia = int(input("Ingrese que dia desea registrar sus gastos"))
    usuario = "patata"
    aux = 0
    while usuario.lower() != "salir":
        usuario = str(input("Ingrese cada gasto que realizo durante el dia, cuando finalice Ingrese SALIR"))
        if usuario.lower() != "salir":
            gasto = int(usuario)
            aux += gasto
        print(gastos)
        gastos[dia-1] = aux
    archivo_de_gastos.writelines(str(gastos))
    archivo.close()
    archivo_de_gastos.close()
ingresar_gastos()
