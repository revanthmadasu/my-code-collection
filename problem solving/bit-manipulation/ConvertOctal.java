import java.util.Scanner;

public class ConvertOctal {
    public static void main(String[] args) {
        System.out.print("Enter base 10 number");
        Scanner scan = new Scanner(System.in);
        int base10 = scan.nextInt();
        int num = base10;
        int base = 8;
        int res = 0, iteration = 0;
        while (num >= base) {
            res += num%base * Math.pow(10, iteration++);
            num /= base;
        }
        res += num%base * Math.pow(10, iteration++);
        System.out.println("Base 8 calculated: " + res + " " + Integer.toOctalString(base10));
        scan.close();
    }
}