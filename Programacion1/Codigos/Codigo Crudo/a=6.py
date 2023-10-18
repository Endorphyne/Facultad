lista = ["14000", "13000", "12000", "6500", "5200", "80000", "30000", "17800", "22000", "7000", "5000", "15000", "17800", "5000", "120000"]
total = 0
for valor in lista:
    if valor.isnumeric():
        total += int(valor)
print('total activos= ', total)
valores = ["8500", "6000", "4000", "2000", "8000", "11400"]
valores_numericos = [int(valor) for valor in valores if valor.isnumeric()]
suma = sum(valores_numericos)
print('total pasivos =', suma)
print('patrimonio neto=', total-suma)