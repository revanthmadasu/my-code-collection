import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        System.out.print("Enter number");
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int res = 0;
        while (num > 0) {
            res *= 10;
            res += num%10;
            num /= 10;
        }
        System.out.println("Reverse calculated: " + res);
        scan.close();
    }
}