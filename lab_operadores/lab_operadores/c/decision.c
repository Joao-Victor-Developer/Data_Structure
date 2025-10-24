#include <stdio.h>
int main() {
    int nota = 72;
    if (nota >= 70) printf("Aprovado com %d\n", nota);
    else if (nota >= 40) printf("Recuperacao com %d\n", nota);
    else printf("Reprovado com %d\n", nota);
    return 0;
}