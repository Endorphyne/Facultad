#1)Lenguaje Python >3.9
#2)Editor de codigo: pycharm o preferencia
#3)Canal de youtube desarrollargo (Unidad:Videos1-6)
#####################TIPOS DE DATOS#####################
#Booleanos(TRUE/FALSE)
#Strings(Cadenas de caracteres)
#Numeros(Enteros(1,2,3)Decimales(1.2,3.4,4.1)Reales/Complejosj))
######################OPERADORES#######################################
#Matematicos(*,**,/,//,%)
#Logicos(AND,OR,NOT)
#Comparacion(<,>,==,<=,>=,!=)
######################EJERCICIOS######################################
##1)Agregar las siguientes expresiones a variables, imprimirlas en consola y explicar cuales son sus tipos de datos:
#1
#100
#True
#1.5
#"1"
#"Python"
#'Python'
#100+50
#100/50.0
#50-8*4
##2)Explicar cuales son los resultados de las siguietns expresiones y por que.
#27.0//2
#27.0/2
#27//2
#27/2
#"27"/2
#True/1
#True/0
#False*2
#False*3
#False//0
#True*"a"
#True!=1
#"hola"*(4/2)
#10-2*4
#(10-2)*4
#2!=2
#2!="2"
#10>10.0
#"a">"b"
#'a'=='a'
#true%1
#1+""+"2"
#"tres"*3
############################################################################################################
a1=1        #int es un numero entero
b1=100      #int es un numero entero
c1=True     #bool es un valor booleano
d1=1.5      #float es un numero decimal
e1="1"      #str es un caracter
f1="Python" #str es una cadena de caracteres
g1='Python' #str es una cadena de caracteres
h1=100+50   #str es una suma de dos enteros
i1=100/50.0 #float es una division entre un entero y un decimal, el decimal hace que la operacion devuelva un resultado de clase float
j1=50-8*4   #int la resta es realizada entre enteros y el resultado de esta dividido no devuelve un decimal sino un entero
peresa = {
    'a1':1,
    'b1':100,
    'c1':True,
    'd1':1.5,
    'e1':"1",
    'f1':"Python",
    'g1':'Python',
    'h1':100+50,
    'i1':100/50.0,
    'j1':50-8*4,
}
for x in peresa:
    print(peresa[x],type(peresa[x]))
peresa2 = {
    'a2':27.0//2,
    'b2':27.0/2,
    'c2':27//2,
    'd2':27/2,
    'e2':"27"/2,
    'f2':True/1,
    'g2':True/0,
    'h2':False*2,
    'i2':False*3,
    'j2':False//0,
    'k2':True*"a",
    'l2':True!=1,
    'm2':"hola"*(4/2),
    "n2":10-2*4,
    'o2':(10-2)*4,
    'p2':2!=2,
    'q2':2!="2",
    'r2':10>10.0,
    's2':"a">"b",
    't2':'a'=="a",
    'u2':True%1,
    'v2':1+""+"2",
    'w2':"tres"*3
}
for x in peresa2:
    print(peresa2[x])