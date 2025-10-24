using System;
class Loop {
    static void Main() {
        for (int i = 1; i <= 5; i++) Console.WriteLine(i);
        int s = 0, j = 1;
        while (j <= 5) { s += j; j++; }
        Console.WriteLine($"Soma = {s}");
        int k = 3;
        do { Console.WriteLine($"k = {k}"); k--; } while (k > 0);
    }
}