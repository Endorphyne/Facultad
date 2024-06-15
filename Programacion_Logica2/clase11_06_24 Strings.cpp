#include<iostream>
#include<cstring>
#define N 100
using namespace std;
int main(){
    // char cad[N];
    // char cad2[N];
    // int diferencia;
    // cout<<"\nIngrese el texto 1: ";
    // cin.get(cad,N-1);
    // cin.get();
    // cout<<cad;
    // cout<< "\nLa cadena 1 esta compuesa por: "<< strlen(cad)<<", caracteres.";
    // cout<<"\nIngrese el texto 2: ";
    // cin.get(cad2,N-1);
    // cout<<cad2;
    // cout<< "\nLa cadena 2 esta compuesa por: "<< strlen(cad2)<<", caracteres.";
    // diferencia = strcmp(cad,cad2);
    // if(diferencia==0)
    // {
    //     cout<<"\nLas cadenas son de igual longitud";
    // }
    // else if(diferencia == 1)
    // {
    //     cout<<"\nLa cadena 2 es mas grande";
    // }
    // else if (diferencia == -1)
    // {
    //     cout<<"\nLa cadena 1 es mas grande";
    // }
    char pass[]="contra",cadena[N];
    do
    {
        cout<<"Ingrese la password\n";
        cin.get(cadena,N-1);
        cin.get();
        cout<<endl;
        if(!strcmp(cadena,pass))
        {
            cout<<"\nClave correcta";
        }
        else
        {
            cout<<"\nClave incorrecta\n";
        }
    } while (strcmp(cadena,pass));
    int i;
    for ( i = 'a';i <= 'z';i++)
    {
        cout<<(char)i<<" ";
    }
    return 0;
}