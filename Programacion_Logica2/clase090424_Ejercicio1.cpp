//1)realiza un algoritmo para determinar si una persona puede votar en base a su edad
#include <iostream>
using namespace std;
int main(){
    int edad;
    cout << "ingrese su edad";
    cin >> edad;
    if (edad >= 16){
        cout << "Puede votar";
    }
    else
    {
        cout << "No puede votar";
    }
}