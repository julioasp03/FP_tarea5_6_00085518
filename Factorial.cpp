#include <iostream>
using namespace std;
int main(){
    int x;
    int factorial=1;
    cout<<"ingrese un numero entero:\n";
    cin>>x;
    for(int i=1;i<=x;i++){
        factorial=factorial*i;
    }
cout<<factorial;
return 0;
}