// 6. Se ingresan las notas de 40 alumnos. Por cada alumno se ingresa:
// a) Numero de matrí cula: 4 dí gitos (1-9999)
// b) Asistencia: 1, presente; 0, ausente
// c) Calificacion: 2 dígitos (0-10).
//  A partir de esta informacion se debe calcular e informar:
// a) Cantidad y porcentaje de alumnos presentes.
// b) Promedio de calificaciones de alumnos presentes y porcentaje de alumnos aprobados (sobre
// el total de alumnos presentes).
// c) Numero de matrí cula del alumno de mayor calificacio n. (Si hay varios alumnos con esa calificacion:
// calificacion y cantidad de alumnos en esa situacion
#include<iostream>
using namespace std;
int main()
{
    const int alumnos = 40;
    int asistencia,matricula,matriculaMayorClasificacion,presentes=0,variosMatrMayorClasi=0;
    float clasificacion,mayorClasificacion,promedioClasificacionPresentes=0,porcentajeAprobados=0;
    for (int x = 1; x<alumnos+1;x++)
    {
        cout << "Ingrese la matricula del alumno Nº"<< x <<"\n:";
        cin >> matricula;
        cout << "\nSu asistencia: (1:Presente/0:Ausente)\n:";
        cin >> asistencia;
            cout << "\nSu nota: (0-10)\n:";
        cin >>clasificacion;
        if (x==1)
        {
            mayorClasificacion = clasificacion;
            matriculaMayorClasificacion = matricula;
        }
        if (clasificacion > mayorClasificacion)
        {
            mayorClasificacion = clasificacion;
            matriculaMayorClasificacion = matricula;
        }
        if (clasificacion >= 6)
        {
            porcentajeAprobados ++;
        }
        if (clasificacion == mayorClasificacion)
        {
            variosMatrMayorClasi++;
        }
        if (asistencia == 1)
        {
            promedioClasificacionPresentes += clasificacion;
            presentes++;
        }
    }
    cout << "Hay "<< presentes << " alumnos presentes (%"<< (static_cast<float>(presentes) / alumnos * 100) << ")\n";
    cout << "El promedio de los presentes es de: "<< promedioClasificacionPresentes/presentes <<"\nEl porcentaje de aprobados sobre los presentes es %"<<(porcentajeAprobados/presentes)*100;
    if (variosMatrMayorClasi > 1)
    {
        cout << "\nHubieron "<< variosMatrMayorClasi<< " alumnos aprobados con la calificacion mas alta: "<< mayorClasificacion;
    }
    else 
    {
        cout << "\nEl alumno con la matricula: "<< matriculaMayorClasificacion << " tuvo la nota mas alta: "<<mayorClasificacion;
    }
}