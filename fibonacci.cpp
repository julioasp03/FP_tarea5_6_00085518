#include <iostream>
using namespace std;
int main(){
int x; int a=0, b=1, c=1;
cout<<"ingrese la cantidad de digitos\n";
cin>> x;
cout<<"0 1 ";
for(int i=1;i<x;i++){
    c=a+b;
    cout<<c<<" ";
    a=b;
    b=c;
}
    return 0;
}