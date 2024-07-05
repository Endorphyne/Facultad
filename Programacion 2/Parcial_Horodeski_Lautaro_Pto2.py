class libro:
    titulo= ""
    autor= ""
    disponible= bool
    def __init__(self,titulo,autor) -> None:
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    def prestar(self):
        self.disponible = False
    def devolver(self):
        self.disponible = True
    def esta_Disponible(self):
        return self.disponible
libro1 = libro("La divina Comedia", "Dante Alighieri") 
libro2 = libro("Main kampf", "Un artista bigoton")
libro3 = libro("Recetas dulces de Tia marita", "Hugo")
libreria = []
libreria.append(libro1)
libreria.append(libro2)
libreria.append(libro3)
print(libreria)
def disponiblitron(estado):
    out = ''
    if estado == True:
        out = "Disponible"
    else: 
        out = "No disponible"
    return out
print("\nListado de libros:")
for x in libreria:
    print(f"Titulo: {x.titulo}, Autor: {x.autor}, Estado: {disponiblitron(x.disponible)}")
print("\nOperaciones:")
libro1.prestar()
print(f"Libro: {libro1.titulo}, prestado")
libro1.devolver()
print(f"Libro: {libro1.titulo}, devuelto")
print("\nEstado de los libros al finalizar las operaciones:")
for x in libreria:
    print(f"Titulo: {x.titulo}, Autor: {x.autor}, Estado: {disponiblitron(x.disponible)}")