#include<iostream>
#define N 5
using namespace std;
char menu();
void cargaVector(int vector[],int vector2[]);
void ordenarVector(int vector[]);
void buscarVector(int vector2[]);
void mostrarVectores(int vector[], int vector2[]);

int main()
{
    bool flag =true;
    int vector[N];
    int vector2[N];
    while (flag)
    {
        switch (menu())
        {
        case '1':
            cargaVector(vector,vector2);
            break;
        case '2':
            ordenarVector(vector);
            break;
        case '3':
            buscarVector(vector2);
            break;
        case '4':
            mostrarVectores(vector,vector2);
            break;
        case 'S':
            flag = false;
            break;
        case 's':
            flag = false;
            break;
        default:
            cout<<"Valor Invalido\n";
            break;
            
        }
    }
}
char menu()
{
    char opcion;
    cout <<"Ingrese la opcion que desea realizar:\n1)Carga\n2)Ordenar\n3)Buscar\n4)Mostrar\nS)Salir\n";
    cin >> opcion;
    return opcion;
}

void cargaVector(int vector[], int vector2[])
{
    int valor=0;
    for (int x = 0; x < N; x++)
    {
        cout <<"Ingrese el valor del vector en la posicion "<<x+1<<" :\n";
        cin >> valor;
        if (valor<11 && valor > -11)
        {
            vector[x] = valor;
        }
        else
        {
            vector[x] = 909090;
        }
        if (valor>11 || valor <- 11)
        {
            vector2[x] = valor;
        }
        else
        {
            vector2[x]=909090;
        }
    }
}
void ordenarVector(int vector[]) 
{ 
    bool bandera = false;
    for (int x =0;x<N;x++)
    {
        if (vector[x] < vector[x+1])
        {
            bandera = true;
        }
    }
    if (bandera)
    {
        cout<<"\nEl vector se encuentra ordenado";
    }
    else
    {
        cout<<"\nEl vector no se encuentra ordenado";
    }
}
void buscarVector(int vector2[])
{
    int valor,pos;
    bool bandera = false;
    cout<<"Ingrese que valor desea buscar en el vector";
    cin >> valor;
    for (int x = 0; x<N;x++)
    {
        if (valor == vector2[x])
        bandera = true;
        pos = x;
        break;
    }
    if (bandera)
    {
        cout<<"\nEl valor se encuentra presente en el vector en la posicion"<<pos;
    }
    else
    {
        cout<<"\nEl valor no se encuentra en el vector";
    }
}
void mostrarVectores(int vec1[],int vec2[])
{
    for (int x = 0; x <2;x++)
    {
        cout<<"\nVector "<<x+1<<":";
        if (x==0)
        {
        for(int i = 0; i<N;i++)
        {
            if (vec1[i] != 909090)
            {
                cout<<vec1[i]<<",";
            }
        }
        }
        else
        {
        for(int i = 0; i<N;i++)
        {
            if (vec2[i] != 909090)
            {
                cout<<vec2[i]<<",";
            }
        }
        }
    }
}