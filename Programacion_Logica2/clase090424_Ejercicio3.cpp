//3)realiza un algoritmo para determinar el costo y el descuento de un articulo, si el precio es >= a 200 se le aplica un descuento del 15%, si el precio es > 100 pero < 200 se le descuenta el 12% y si es < 100 no se le aplica descuento
#include <iostream>
using namespace std;
int main(){
    float precio;
    cout << "Ingrese el valor del producto";
    cin >> precio;
    if (precio>= 200){
        precio = precio * 0.85;
        cout << "Se le aplico un descuento del 15%";
    }
    else{
        if (precio > 100 && precio < 200){
            precio = precio * 0.88;
            cout << "Se le aplico un descuento del 12%";
        }
        else{
            cout << "No se aplico ningun descuento";
        }
    };
    cout << "\nEl precio es de: $", cout << precio;
}