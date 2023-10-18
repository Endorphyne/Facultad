semana = {
    "Lunes":32500,
    "Martes":47830,
    "Miertcoles":24550,
    "Jueves":40032,
    "Viernes":23210,
    "Sabado": 17990,
}
VentasOrdenadas = sorted(semana.items(), key = lambda x:x[1])
diaDeMayorVenta = VentasOrdenadas[-1]
VentasSemanaOrdenadas = list(semana.values())
VentasSemanaOrdenadas.sort(reverse = True) #Ventas ordenadas de mayor a menor
promedioVentas=0 
for x in range(len(VentasSemanaOrdenadas)) :
    promedioVentas = VentasSemanaOrdenadas[x] + promedioVentas
print("El promedio de ventas es de:", promedioVentas/len(VentasSemanaOrdenadas), ", el total de:", promedioVentas, "y el dia con mas ventas el:", diaDeMayorVenta[0], " con un total de:", diaDeMayorVenta[1] )