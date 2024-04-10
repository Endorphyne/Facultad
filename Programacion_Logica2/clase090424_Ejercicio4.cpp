//4)realiza un algoritmo con base a una clasificacio (0-10) que indique con una letra la clasificacion que le corresponde: 10=A,9=B,8=C,7/6=D,5-0=F
#include <iostream>
using namespace std;
int main(){
    float nota;
    string clasificacion;
    cout << "Ingrese la nota\n Nota:";
    cin >> nota;
    if (nota <= 5){
        clasificacion = "F";
    }
    else{
        if (nota==6 || nota == 7){
            clasificacion = "D";
        }
        else{
            if (nota==8){
                clasificacion = "C";
            }
            else{
                if (nota == 9){
                    clasificacion = "B";
                }
                else{
                    clasificacion = "A";
                };
            };
        };
    };
    cout << "\n La clasificacion es: " + clasificacion;
}