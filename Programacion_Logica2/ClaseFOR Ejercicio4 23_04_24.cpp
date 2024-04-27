#include<iostream>
using namespace std;
int main(){
    int N, Y;
    bool bandera;
    bandera = true;
    cout << "Ingrese el primer valor: \n";
    cin >> N;
    for (int x = 0;x<4;x++){
        cout << "Ingrese numero superior al anterior por un valor \n";
        cin >> Y;
        if (Y != N+1){
            bandera = false;
        }
        N++;
    }
    if (bandera){
        cout<< "Numeros Ordenados ascendentemente";
    }
    else{
        cout<<"Numeros no ordenados";
    }
}