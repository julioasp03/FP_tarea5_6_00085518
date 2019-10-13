#include <iostream>
using namespace std;
int main(){
int total;
cout<<"ingrese el total de datos\n";
cin>>total;
float aux, suma=0;
for(int i=0;i<total;i++){
    cout<<"ingrese el digito "<<(i+1)<<":";
    cin>>aux;
    suma+=aux;
}
cout<<"el valor de la media es: "<<suma;

    return 0;
}