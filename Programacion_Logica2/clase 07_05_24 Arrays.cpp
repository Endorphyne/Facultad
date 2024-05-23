#include<iostream>
using namespace std;
int main()
{
    //declaracion de un vector
    // int (tipo de dato); vector (nombre del vector)[x]cantidad de posiciones de memoria asignadas al vector
    // se accede a cada celda por indice iniciando en 0 solamente, no se puede acceder al vector en su totalidad al mismmo tiempo
    //
    int vector[5];
    for(int x =0;x<5;x++)
    {
        cout<<"ingrese un valor para el vector en la posicion: "<<x<<"\n";
        cin >> vector[x];
    }
    for(int x =0;x<5;x++)
    {
        cout<<"En la posicion("<<x<<") el vector tiene el valor: "<<vector[x]<<'\n';
    }
}