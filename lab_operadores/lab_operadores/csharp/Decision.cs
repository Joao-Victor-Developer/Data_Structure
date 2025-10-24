using System;
class Decision {
    static void Main() {
        int nota = 72;
        if (nota >= 70) Console.WriteLine($"Aprovado com {nota}");
        else if (nota >= 40) Console.WriteLine($"Recuperacao com {nota}");
        else Console.WriteLine($"Reprovado com {nota}");
    }
}