#include<iostream>
using namespace std;
int main()
{
    long long int limite, primer=0,segundo=1,siguiente;
    cout<< "Ingrese el limite de la siete fibbonnacci";
    cin >> limite;
    for (int x = 1; x<limite+1;x++)
    {
        if (x == primer)
        {
            cout << primer << ", ";
            continue;
        }
        if (x == segundo)
        {
            cout << segundo << ",";
            continue;
        }
        //segmento de incremento fibbo
        siguiente = primer + segundo;
        primer = segundo;
        segundo = siguiente;
        
        cout << siguiente;
        if (x != limite)
        {
            cout<<",";
        }
    }
    cout << endl;
}