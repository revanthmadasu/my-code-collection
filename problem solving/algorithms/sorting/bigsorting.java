/*
https://www.hackerrank.com/challenges/big-sorting/problem
*/
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
public class Solution {

    static class MyComparator implements Comparator<String> {
        public int compare(String first_Str, String second_Str) {
            int firstLen = first_Str.length();
            int secondLen = second_Str.length();
            return firstLen == secondLen ? first_Str.compareTo(second_Str) : (
                firstLen > secondLen ? 1 : -1 
            );
        }
    }
    // Complete the bigSorting function below.
    static String[] bigSorting(String[] unsorted) {
        TreeSet<String> nums = new TreeSet(
            new MyComparator()
        );
        HashMap<String, Integer> numsCountMap = new HashMap();
        for (String numS: unsorted) {
            nums.add(numS);
            if (numsCountMap.containsKey(numS)) {
                numsCountMap.put(numS, numsCountMap.get(numS)+1);
            } else {
                numsCountMap.put(numS, 1);
            }
        }
        ArrayList<String> sortedNumsS = new ArrayList();
        for(String num: nums) {
            System.out.println(num);
            int count = numsCountMap.get(num);
            for (int i=0;i<count; ++i) {
                sortedNumsS.add(num);
            }
        }
        return sortedNumsS.stream().toArray(String[] ::new);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] unsorted = new String[n];

        for (int i = 0; i < n; i++) {
            String unsortedItem = scanner.nextLine();
            unsorted[i] = unsortedItem;
        }

        String[] result = bigSorting(unsorted);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(result[i]);

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
