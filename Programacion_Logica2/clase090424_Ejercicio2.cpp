//2)realiza un algoritmo para determinar el sueldo semanal de un trabajador en base a las horas trabajadas y el pago por hora considerando que si trabajo mas de 40 horas se le paga el doble
#include <iostream>
using namespace std;
int main(){
    int horas_Trabajadas;
    float paga, valor_Hora;
    paga = 0;
    cout << "Ingrese el valor de la hora Trabajada: ";
    cin >> valor_Hora;
    cout << "Ingrese la cantidad de horas trabajadas: ";
    cin >> horas_Trabajadas;
    if (horas_Trabajadas > 40){
        paga = paga + (40 * valor_Hora);
        paga = paga + ((valor_Hora * 2) * (horas_Trabajadas - 40));
    }
    else {
        paga = paga + (valor_Hora * horas_Trabajadas);
    }
    cout << "La paga es de:$", cout<< paga;
}