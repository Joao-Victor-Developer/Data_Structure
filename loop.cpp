#include <iostream>
using namespace std;
int main() {
    for (int i = 1; i <= 5; ++i) cout << i << endl;
    int s = 0, j = 1;
    while (j <= 5) { s += j; j++; }
    cout << "Soma = " << s << endl;
    int k = 3;
    do { cout << "k = " << k << endl; k--; } while (k > 0);
    return 0;
}