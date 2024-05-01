#include<iostream>
#include<math.h>
using namespace std;
// =============================================EJERCICIO1======================================================
// int main()
// {
//     float valor=0,valor1=0,input = 0;
//     while (valor < 100)
//     {
//         cout << "Ingrese un valor ";
//         cin >> input;
//         valor += input;
//         if (valor < 100)
//         {
//             valor1 += input;
//         }
//     }
//     cout << "\nEl valor supero 100. Pero antes valio: "<<valor1;
// }
// =============================================EJERCICIO2======================================================
// int main()
// {
//     //Ecuacion = Ax^2+Bx+C
//     float A=1,B=1,C=1,x=0,resultado;
//     double termino1;
//     while (x != 99)
//     {
//         cout<<"\nIngrese un valor para X (99 si desea salir del programa): ";
//         cin >> x;
//         if (x == 99)
//         {
//             continue;
//         }
//         else
//         {
//             termino1 = pow((A*x),2);
//             resultado = termino1+(B*x)+C;
//             cout << "La ecuacion (A(x)^2+B(x)+C)da por resultado= "<< resultado;
//         }
//     }
// }
// =============================================EJERCICIO3======================================================
// int main()
// {
//     float input,promedio=0,total=0,oka=0;
//     while (total<100)
//     {
//         cout<<"\nIngrese un valor: ";
//         cin >> input;
//         if (input==0)
//         {
//             oka++;
//             cout<<"\nOKA!!!(ingreso '0')";
//         }
//         else
//         {
//             oka++;
//             total += input;
//             promedio = total /oka;
//         }
//         cout<<"\nEl total de numeros ingresados es de: "<<oka<<"\nEl promedio es de: "<<promedio<<"\nEl total es de: "<< total;
//         if (total >= 100)
//         {
//             cout << "\nBYE BYE!!";
//         }
//     }
// }
int main()
{
    char input;
    float nota,cantidad_Alumnos,alumnos_Aprobados=0,total_Alumnos, total_Notas;
    bool bandera=true;
    do
    {
        cout<<"\n1. Cantidad de aprobados y desaprobados.\n2. Promedio de notas.\nS. Salir \n:";
        cin >> input;
        switch (input)
        {
        case '1':
            cout <<"\nIngrese la cantidad de alumnos que realizaron el parcial\n:";
            cin >>cantidad_Alumnos;
            for (int x = 1;x<=cantidad_Alumnos;x++)
            {
                cout << "\nIngrese la nota del alumno N("<<x<<")\n:";
                cin >> nota;
                if (nota >= 0 && nota <= 10)
                {                
                        if (nota >= 6)
                        {
                            alumnos_Aprobados++;
                        }
                }
                else 
                {   
                    x--;
                    cout << "\nValor invalido";
                }
            }
            cout<<"\nLa cantidad de alumnos aprobados fue de: "<<alumnos_Aprobados<<"\nLa cantidad de alumnos desaprobados fue de: "<< cantidad_Alumnos-alumnos_Aprobados;
            break;
        case '2':
            total_Alumnos=0;
            total_Notas=0;
            cout<<"Empieze la carga de notas(Ingrese '99' para salir)\n:";
            cin >> nota;
            while (nota != 99)
            {
                cin >> nota;
                if (nota==99)
                {
                    break;
                }
                else
                {
                    total_Alumnos++;
                    total_Notas+=nota;
                }
            }
            cout << "El promedio de notas es de: "<< total_Notas/total_Alumnos;
            
            break;
        case 's':
            bandera = false;
        case 'S':
            bandera = false;
        default:
            break;
        }
    } while (bandera);
}