semana = ["Lunes", "Martes", "Miercoles", 'Jueves', 'Viernes', 'Sabado', 'Domingo']
for x in range(len(semana)):
    print(semana[x])
    if semana[x] == 'Viernes':
        print('Por fin es viernes, hora del vicio')
        break