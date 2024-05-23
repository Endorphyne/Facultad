#include<iostream>
using namespace std;
int main()
{
    // ==========================EJERCICIO1=====================================
    // float numeros[10];
    // for (int x =0;x<10;x++)
    // {
    //     cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
    //     cin >> numeros[x];
    // }
    // for (int x = 0;x<10;x += 2)
    // {
    //     cout<< numeros[x]<<","<<numeros[x+1]<<"\n";
    // }
    // ==========================EJERCICIO2-3=====================================
    // int numeros[10];
    // for (int x =0;x<10;x++)
    // {
    //     cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
    //     cin >> numeros[x];
    // }
    // for (int x = 0;x<10;x++)
    // {
    //     if(numeros[x]%2 !=0)
    //     {
    //         cout<<"Valor impar: "<<numeros[x]<<"\n";
    //     }
    //     if (x%2 == 0)
    //     {
    //         cout<<"Indice par: "<<numeros[x]<<"\n";
    //     }
    // }
    // ==========================EJERCICIO4=====================================
    //      int acumulador=0, numeros[10],valor_Buscar;
    //     for (int x =0;x<10;x++)
    //     {
    //         cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
    //         cin >> numeros[x];
    //     }
    //     cout<<"Ingrese que numero desea buscar en el vector\n";
    //     cin >> valor_Buscar;
    //     for(int x =0; x<10;x++)
    //     {
    //         if (numeros[x]==valor_Buscar)
    //         {
    //             acumulador++;
    //         }
    //     }
    //     cout<<"El numero aparece: "<<acumulador<<" veces\n";
    // }   
    // int limite_I,limite_S,numeros[10];
    // for (int x =0; x<10;x++)
    // {
    //     cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
    //     cin >> numeros[x];   
    // }
    // cout<<"Ingrese 2 numeros para definir el intervalo de busqueda:\nLimite Inferior:";
    // cin >> limite_I;
    // cout<<"\nLimite Superior:";
    // cin >> limite_S;
    // limite_S++;
    // for (limite_I;limite_I<limite_S;limite_I++)
    // {
    //     cout<<"Posicion ("<<limite_I+1<<") valor: "<< numeros[limite_I]<<"\n";
    // }
    // int numeros[10];
    // bool bandera;
    // bandera = true;
    // for (int x = 0; x<10;x++)
    // {
    //     cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
    //     cin >> numeros[x];
    // }
    // for (int x = 0;x<9;x++){
    //     if (numeros[x] >= numeros[x+1]){
    //         bandera = false;
    //     }
    // }
    // if (bandera){
    //     cout<< "Numeros Ordenados ascendentemente";
    // }
    // else{
    //     cout<<"Numeros no ordenados";
    // }
    int vector_A[10],vector_B[10],vector_C[10];
    for (int x = 0; x<10;x++)
    {
        cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
        cin >> vector_A[x];
    }
    for (int x = 0; x<10;x++)
    {
        cout<<"Ingrese un numero para la posicion("<<x+1<<")\n";
        cin >> vector_B[x];
    }
    for (int x = 0; x<10;x++)
    {
        vector_C[x] = vector_A[x]+vector_B[x];
    }
    for (int x = 0; x<10;x++)
    {
        cout<<"La suma de los vectores en la posicion ("<<x+1<<") es: "<<vector_C[x]<<"\n";
    }
}