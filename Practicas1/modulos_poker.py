def armar_mazo():
    mazo1 = []
    palos = ["Trebol","Pica","Diamante","Corazones"]
    for x in palos:
        for i in range(2,15):
            if i == 14 :
                mazo1.append(str(f"AS de {x}"))
            elif i == 11:
                mazo1.append(str(f"J de {x}"))
            elif i == 12:
                mazo1.append(str(f"Q de {x}"))
            elif i == 13:
                mazo1.append(str(f"K de {x}"))
            else:
                mazo1.append(str(f"{i} de {x}"))
    mazo2 = {}
    valor = 1
    for x in mazo1:
        if valor == 13:
            valor = 1
        mazo2.update({x:valor})
        valor += 1
    return(mazo2)
# def desarmar_mano(mano):
#     mano = str(mano)
#     mano_dividida = mano.split(" ")
#     mano2 = ""
#     for x in mano_dividida:
#         if x != "de":
#             mano2 += (f"{x} ")
#     return mano
armar_mazo()
def jugadas(manoJ, ManoC ):
    valor_Jugador = 0
    valor_Computadora = 0
    carta_Alta_J = 0
    carta_Alta_C = 0

mazo = armar_mazo()
print(mazo)