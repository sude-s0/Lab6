#include <iostream>

using namespace std;


double h_Function(int n) {
    if(n==1){
        return 1;
    }
    else {
        return 1.0/n + h_Function(n-1);
    }


}

double h_Function(){
    int n;
    cout << "Enter n: ";
    cin >> n;
    return h_Function(n);
    }


int main(){

   
    return 0;
}
