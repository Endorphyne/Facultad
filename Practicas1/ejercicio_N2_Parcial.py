resultado = {
    "a" : 0,
    "b" : 0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0
}
frase = str(input("Ingrese una frase:"))
frase = frase.lower()
for x in frase:
    if x in resultado:
        resultado[x] += 1
for x,y in resultado.items():
    if y > 1 or y == 0:
        print(f"{x}:{y} veces")
    else:
        print(f"{x}:{y} vez")
