milista=[]
notas=[]

x=input("quiere ingresar una materia S/N: ")
while x=='s' or x=='S':
    milista.append(input("ingrese la materia: "))
    notas.append(float(input("ingrese la nota: ")))
    a=input("quiere ingresar otra materia S/N: ")
    if(a=='N' or a=='n'):
        x=False

i=0
for milista in milista:
    if (notas[i]>=6):
        milista.pop(i)
        notas.pop(i)
    i=i+1

i=0
for milista in milista:
    print("materia a recursar:",milista," nota:",notas[i])
    i=i+1