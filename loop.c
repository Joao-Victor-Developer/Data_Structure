#include <stdio.h>
int main() {
    for (int i = 1; i <= 5; i++) printf("%d\n", i);
    int s = 0, j = 1;
    while (j <= 5) { s += j; j++; }
    printf("Soma = %d\n", s);
    int k = 3;
    do { printf("k = %d\n", k); k--; } while (k > 0);
    return 0;
}