#include<iostream>
using namespace std;
int main(){
    int x,y;
    cout << "Ingrese el primer numero\n";
    cin >> x;
    cout << "Ingrese el segundo numero\n";
    cin >> y;
    cout << x << "X" << y << "=" << x*y;
    cout << "\n";
    for (int i = 0; i<x;i++ ){
        cout << y;
        if (i== x-1){
            cout  << " = " << x*y;
        }
        else{
            cout << " + ";
        }
    }
    cout << "\n";
    for (int i = 0; i<y;i++ ){
    cout << x;
    if (i== y-1){
        cout  << " = " << x*y;
    }
    else{
        cout << " + ";
    }
}
}