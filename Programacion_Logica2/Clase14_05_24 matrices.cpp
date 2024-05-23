#include<iostream>
#define fila1_1 4
#define columna_1 4
#include<random>
using namespace std;
int main()
{
    int matriz[fila1_1][columna_1], valor;
    for (int x = 0; x<fila1_1; x++)
    {
        for (int i =0 ;i<columna_1;i++)
        {
            cout<< "\nIngrese un valor para la posicion ["<<x<<"]["<<i<<"] del vector\n";
            valor = rand();
            if (valor < 0 || valor > 9)
            {
                cout << "\nValor invalido\n";
                i--;
            }
            else
            {
                matriz[x][i] = valor;
            }
        }
    }
    for (int x= 0;x<fila1_1;x++)
    {
        for (int i = 0; i <columna_1; i++)
        {
            cout << matriz[x][i];
            cout <<",";
        }
        cout<< endl;
    }
}