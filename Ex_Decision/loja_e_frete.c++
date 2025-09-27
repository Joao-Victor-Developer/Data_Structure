#include <iostream>
using namespace std;


int main() 
{
    cout << "Hello, World!";
    float value;

    cout << "Enter the value of the product: ";
    cin >> value;

    float freight = 15;
    cout << "The freight value is: " << freight << endl;

if (value >= 100) {
    freight =  0;
    cout << "The freight value is free: " << freight << endl;
}
else{

    freight = value + 15;
    cout << "The product with freight value is: " << freight << endl;


}
    return 0;
}