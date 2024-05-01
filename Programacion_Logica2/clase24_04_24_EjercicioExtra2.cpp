#include<iostream>
using namespace std;
int main()
{
    int cantidadNegativos, cantidadMayor50, cantidadEntre25y45;
    float numero;
    cantidadNegativos = 0;
    cantidadEntre25y45 = 0;
    cantidadMayor50 = 0;
    for (int x = 1; x < 10; x++)
    {
        cout << "Ingrese un numero: \n";
        cin >> numero;
        if (numero < 0)
        {
            cantidadNegativos++;
        }
        else if (numero > 50)
        {
            cantidadMayor50++;
        }
        else if (numero >= 25 && numero <= 45)
        {
            cantidadEntre25y45++;
        }
    }
    cout << "\nLa cantidad de negativos fue de: ", cout<< cantidadNegativos;
    cout << "\nLa cantidad de Mayores de 50 fue de: ", cout<< cantidadMayor50;
    cout << "\nLa cantidad de numeros entre 25 y 45 fue de: ", cout<< cantidadEntre25y45;
}