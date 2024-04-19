socios = {}
bandera = 0
while bandera < 3:
    try:
        print("Ingrese el nombre y el monto que aporto el socio")
        socio = input("NOMBRE:").lower()
        socio == str
        monto = float(input("MONTO:"))
        socios.update({socio:monto})
        bandera +=1
    except ValueError:
        print("Valor ingresado invalido")
total = 0
for valor in socios.values():
    total += valor
for x,y in socios.items() : 
    print(f"El socio {x.capitalize()}, aporto: ${y} lo que compone un %{round((y*100)/total,2)}")