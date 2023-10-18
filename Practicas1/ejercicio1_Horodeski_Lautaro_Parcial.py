import random
def dados():
    jugador = 0
    dadoJ = []
    computadora = 0
    dadoC = []
    def lanzamiento():
        return random.randint(1,6)
    for x in range(2):
        lanzada1 = lanzamiento()
        lanzada2 = lanzamiento()
        jugador += lanzada1
        dadoJ.append(lanzada1)
        computadora += lanzada2
        dadoC.append(lanzada2)
    if jugador > computadora :
        ganador = "Usuario"
    elif computadora > jugador :
        ganador = "Computadora"
    else:
        ganador = "Empate"
    if ganador == "Empate":
        print(f"El usuario saco {jugador} ({dadoJ[0]} + {dadoJ[1]})\nLa computadora {computadora} ({dadoC[0]} + {dadoC[1]})\nFue un empate")
    else:
        print(f"El Usuario saco {jugador} ({dadoJ[0]} + {dadoJ[1]})\nLa Computadora {computadora} ({dadoC[0]} + {dadoC[1]})\nEl ganador es {ganador}")
dados()