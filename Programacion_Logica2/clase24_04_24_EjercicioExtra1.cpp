#include<iostream>
using namespace std;
int main()
{
    float min,valor, max, posMax;
    cout<<"Ingrese un valor";
    cin >> min;
    max = min;
    for(int i = 2; i < 11; i++)
    {
        cout << "\nIngrese otro valor";
        cin >> valor;
        if (valor > max)
        {
            max=valor;
            posMax = i;
        }
        else if (valor < min)
        {
            min = valor;   
        }
    }
    cout << "\nEl valor maximo fue: ", cout << max,cout << " Con la posicion: ", cout << posMax, cout << "\nEl valor minimo fue: ", cout << min;
}