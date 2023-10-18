def diaDeSemana(a):
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    if 1 <= a <= 7:
        return dias_semana[a - 1]  # Restamos 1 para acceder al índice adecuado en la lista
    else:
        return "Día no válido"
def calculadoraTiempo(dias:int):
# Esta función toma un argumento entero dias, que representa la cantidad de días que se desea convertir en años, meses y días.
# Inicializa las variables años y meses en 0.
# Luego, utiliza la división entera (//) para calcular la cantidad de años en dias y reduce dias en consecuencia.
# Después, calcula la cantidad de meses en los días restantes y también reduce los días en consecuencia.
# La función devuelve una tupla que contiene la cantidad de años, meses y días calculados.
    años    = 0
    meses   = 0
    años = dias//360
    dias -= años*360
    meses = dias//30
    dias -= meses*30
    return(años, meses, dias)
def calculadoraTiempo2(segundos:int):
# Esta función toma un argumento entero segundos, que representa la cantidad de segundos que se desea convertir en años, meses, días, horas, minutos y segundos.
# Inicializa las variables años, meses, dias, horas, minutos y segundos en 0.
# Utiliza la división entera (//) para calcular la cantidad de años en segundos y reduce segundos en consecuencia.
# Luego, calcula la cantidad de meses en los segundos restantes y reduce los segundos en consecuencia.
# Después, calcula la cantidad de días en los segundos restantes y continúa con la misma lógica para horas, minutos y segundos.
# La función devuelve una tupla que contiene la cantidad de años, meses, días, horas, minutos y segundos calculados.
    años    = 0
    meses   = 0
    años = segundos//933120000
    segundos -= años*933120000
    meses = segundos//2592000
    segundos -= meses*2592000
    dias = segundos //86400
    segundos -= dias*86400
    horas = segundos//3600
    segundos -= horas*3600
    minutos = segundos//60
    segundos -= minutos *60
    return(años, meses, dias,horas,minutos,segundos)