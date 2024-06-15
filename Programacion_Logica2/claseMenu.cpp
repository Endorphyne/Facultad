#include<iostream>
using namespace std;
#include<algorithm>
#define filas 4
#define columnas 5
char menu();
int** cargaMatriz();
int* copiarColumna(int**, int);
void ordenarFila(int**,int);
bool cerofiquinador(int*,int);

int main()
{
    int** matrizCargada;
    int* columnaCopiada;
    int columnaDeseada;
    bool bandera=true,cero;
    while (bandera)
    {
    switch (menu())
    {
    case '1':
        matrizCargada = cargaMatriz();
        break;
    case '2':
        int filaDeseada;
        cout << "Ingrese la fila que desea ordenar: ";
        cin >> filaDeseada;
        filaDeseada = filaDeseada -1;
        if(filaDeseada >= 0 && filaDeseada < filas) {
            ordenarFila(matrizCargada, filaDeseada);
        } else {
            cout << "Índice de fila inválido.\n";
        }
        break;
    case '3':
        cout<<"Ingrese la columna que desea copiar a un vector\n";
        cin>> columnaDeseada;
        columnaDeseada = columnaDeseada - 1;
        columnaCopiada = copiarColumna(matrizCargada,columnaDeseada);
        for (int x=0;x<=filas;x++)
        {
            cout<<columnaCopiada[x]<<",";
        }
        break;
    case '4':
        cero = cerofiquinador(columnaCopiada,columnas);
        if(cero)
    {
        cout << "El valor 0 esta presente en el array.\n";
    }
    else
    {
        cout << "El valor 0 no esta presente en el array.\n";
    }
        break;
    case 'S':
        bandera = false;
        break;
    case 's':
        bandera = false;
        break;
    default:
        cout<<"\n Valor ingresado invalido";
        break;
    }
    }
}
char menu()
{
    char opcion;
    cout <<"Ingrese la opcion que desea realizar:\n1)Carga\n2)Ordenar\n3)Vector\n4)Buscar\nS)Salir\n";
    cin >> opcion;
    return opcion;
}
int** cargaMatriz()
{
    int** matriz = new int*[filas];
    for(int i = 0; i <= filas; i++){
        matriz[i] = new int[columnas];
    }
    for(int i = 0; i <= filas; i++) {
        for(int j = 0; j < columnas; j++) {
            cout << "Ingrese el elemento en la posicion (" << i+1 << ", " << j+1 << "): ";
            cin >> matriz[i][j];
        }
    }
    return matriz;
}
void ordenarFila(int** matriz, int fila)
{
    if(fila >= 0 && fila < filas) {
        std::sort(matriz[fila], matriz[fila] + columnas);
    }
    else
    {
        cout<<"Indice de fila invalido.\nIngrese otro:\n";
        cin>>fila;
    }
    for (int x =0; x <= filas;x++){
        cout<<matriz[fila][x]<<',';
    }
}
int* copiarColumna(int** matriz, int columnaDeseada) {
    int* columna = nullptr;
    if(columnaDeseada >= 0 && columnaDeseada < columnas) {
        columna = new int[filas];
        for(int i = 0; i <= filas; i++) {
            columna[i] = matriz[i][columnaDeseada];
        }
    } else {
        cout << "Indice de columna invalido.\n";
    }
    return columna;
}
bool cerofiquinador(int* columnaCopiada, int size)
{
    bool cero = false;
    for (int x = 0; x <= size; x++)
    {
        if(columnaCopiada[x] == 0)
        {
            cero = true;
            break;
        }
    }
    return cero;
}
