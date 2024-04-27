#include<iostream>
using namespace std;
int N, pares, impares;
int main(){
    cout<< "Ingrese el numero limite: \n";
    cin >> N;
    pares = 0;
    impares = 0;
    for (int x = 1;x<=N;x++){
        if(x%2 == 0){
            pares = pares + x;
        }
       else{
            impares = impares + x;
    }
    }
    cout <<"Par= " << pares;
    cout <<"\nImpar= "<<impares;
}