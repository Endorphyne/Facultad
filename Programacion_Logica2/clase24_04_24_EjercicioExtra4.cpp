#include<iostream>
using namespace std;
int main()
{
    float suma,nose;
    suma = 0;
    nose = 1;
    for (int x = 1; x <101; x++)
    {
        //acumulador
        suma = suma + nose;
        //modificacion del nose
        nose = nose * (-1)/3;
    }
    cout << "La suma de los primeros 100 valores de la serie es: " << suma;
}