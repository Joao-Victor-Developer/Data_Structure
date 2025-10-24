using System;
class Arithmetic {
    static void Main() {
        int a = 12, b = 5;
        Console.WriteLine($"a = {a}, b = {b}");
        Console.WriteLine($"Soma: {a + b}");
        Console.WriteLine($"Divisao real: {(double)a / b}");
        Console.WriteLine($"Resto: {a % b}");
    }
}