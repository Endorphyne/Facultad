#include <iostream>
#include <cmath>
using namespace std;
//================================Ejercicio1=================================================
// hacer un programa que muestre que vocal ha sido ingresada
//================================Ejercicio3=================================================
// escribir un programa a modo de calculadora que permita al usuario mostrar un menu con las siguientes opciones 1) suma, 2) resta, 3) producto, 4) division, 5) raiz cuadrada(sqrt()), 6) potencia(pow(a,b)), S) Salir del programa (lib c math)
//================================Ejercicio4=================================================
// escribir un programa para guardar el resultado de la division de dos enteros se va a necesitar de una variable de tipo flotante, el denominador no puede ser 0, si eso ocurre mostrar un error y salir del programa
int main(){
    char letra;
    cout << "Ingrese una letra para saber que vocal es\n :";
    cin >> letra;
    switch (letra=std::tolower(letra))
    {
    case 'a':
        cout << "\n La vocal es A";
        break;
    case 'e':
        cout << "\n La vocal es E";
        break;
    case 'i':
        cout << "\n La vocal es I";
        break;
    case 'o':
        cout << "\n La vocal es O";
        break;
    case 'u':
        cout << "\n La vocal es U";
        break;
    default:
        cout << "\n Valor ingresado invalido o no es vocal";
        break;
    }
    return 0;
}
