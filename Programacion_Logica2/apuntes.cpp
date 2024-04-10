// ingresar un numero y mostrar por pantalla si el numero ingresado es positivo o negativo
#include <iostream>
using namespace std;
int main()  
    {int A;
    cout << "Ingrese un numero" ;
    cin >> A;
    if (A == 0)
        {
            cout << "El numero es igual a 0";
        }
    else
        {
        if (A>0)
        {
            cout << "El numero es positivo";
        }
        else
            {
                cout << "El numero es negativo";
            }
        };}