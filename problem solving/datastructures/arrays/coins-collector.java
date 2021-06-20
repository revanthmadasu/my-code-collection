/**
    hackerearth elean solutions
*/

import java.io.*;
import java.util.*;


public class TestClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
         int N = Integer.parseInt(br.readLine().trim());
         String[] arr_A = br.readLine().split(" ");
         int[] A = new int[N];
         for(int i_A = 0; i_A < arr_A.length; i_A++)
         {
         	A[i_A] = Integer.parseInt(arr_A[i_A]);
         }

         long out_ = maximumCoins(N, A);
         System.out.println(out_);

         wr.close();
         br.close();
    }
    static long maximumCoins(int N, int[] A){
        long result = 0;
        int firstLeastIndex = 0;
        for (int i=0; i<N; ++i) {
            if (A[firstLeastIndex] > A[i]) {
                firstLeastIndex = i;
            }
        }
        long leastNum = A[firstLeastIndex];
        result += (leastNum * N);
        result += (firstLeastIndex);
        return result;
    }
}
