public class Decision {
    public static void main(String[] args) {
        int nota = 72;
        if (nota >= 70) System.out.println("Aprovado com " + nota);
        else if (nota >= 40) System.out.println("Recuperação com " + nota);
        else System.out.println("Reprovado com " + nota);
    }
}