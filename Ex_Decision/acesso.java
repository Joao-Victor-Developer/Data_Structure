
import java.util.Scanner;
public class acesso {
    

public static void main(String[] args) {

    Scanner reader = new Scanner(System.in);
    String code, user;
    System.out.println(" Digite a senha: ");
    code = reader.next();
    System.out.println(" Digite a conta: ");
    user = reader.next();
    
    if (code.equals("admin1234")) {
        System.out.println("Bem vindo, administrador");
    }
    else if (user.equals("user123")) {
        System.out.println("Bem vindo, usuário");
    } 
    else {
        System.out.println("Acesso Negado");
    }






}
}