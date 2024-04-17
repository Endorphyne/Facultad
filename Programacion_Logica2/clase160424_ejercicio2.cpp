//================================Ejercicio2==============================================
// construya un programa que al recibir como dato el cargo de un profesor asi como su salario, incremente este ultimo siguiendo las siguientes especificaciones: Adjunto : 3.5%, Auxiliar: 4.1%, Asistente: 4.8% y Titular 5.3%
#include<iostream>
#include<cctype>
using namespace std;
int main(){
    float salario;
    char cargo;
    bool bandera;
    cout << "Ingrese el cargo:\n A) Adjunto\n B) Auxiliar \n C) Asistente\n D) Titular\n :";
    cin >> cargo;
    string puesto;
    bandera = false;
    if (cargo == 'a' || cargo == 'b' || cargo == 'c' || cargo == 'd'){
        cout << "Ingrese el salario.";  
        cout << "\n :";
        cin >> salario;
        bandera = true;
    }
    else{
        cout << "valor INVALIDO";
    }
    switch (cargo = std :: tolower(cargo))
    {
    case 'a' :
        puesto = "Adjunto";
        salario = salario + (salario * 0.035);
        break;
    case 'b' :
        puesto = "Auxiliar";
        salario = salario + (salario * 0.041);
        break;
    case 'c':
        puesto = "Asistente";
        salario = salario + (salario * 0.048);
        break;
    case 'd':
        puesto = "Titular";
        salario = salario + (salario * 0.051);
        break;
    default:
        cout << "Valor ingresado invalido";
        break;
    }
    if (bandera){
    cout << "\n El salario de: ";
    cout << puesto;
    cout << "\n Es de: ";
    cout << "$";
    cout<< salario;
    }
    return 0;
}