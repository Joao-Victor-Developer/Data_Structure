#include <iostream>
using namespace std;
int main() {
    int nota = 72;
    if (nota >= 70) cout << "Aprovado com " << nota << endl;
    else if (nota >= 40) cout << "Recuperacao com " << nota << endl;
    else cout << "Reprovado com " << nota << endl;
    return 0;
}