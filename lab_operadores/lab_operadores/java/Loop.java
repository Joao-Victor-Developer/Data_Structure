public class Loop {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) System.out.println(i);
        int soma = 0, j = 1;
        while (j <= 5) { soma += j; j++; }
        System.out.println("Soma = " + soma);
        int k = 3;
        do { System.out.println("k = " + k); k--; } while (k > 0);
    }
}