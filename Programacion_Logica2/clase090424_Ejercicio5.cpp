//5)realiza un algoritmo que lea dos numeros x e y si x > y realizar la diferencia caso contrario la suma
#include <iostream>
using namespace std;
int main(){
    float x, y, res;
    cout << "Ingrese X\n";
    cin >> x;
    cout << "\nIngrese Y\n";
    cin >> y;

    if (x>y){
        res = x-y; 
    }
    else{
        res = x+y;
    };
    cout << "\n El resultado es: ", cout << res;
}