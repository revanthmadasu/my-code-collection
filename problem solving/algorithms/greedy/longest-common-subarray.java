import java.io.*;
import java.util.*;


public class TestClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for(int t_i = 0; t_i < T; t_i++)
        {
            int M = Integer.parseInt(br.readLine().trim());
            int N = Integer.parseInt(br.readLine().trim());
            int[][] A = new int[M][N];
            for(int i_A = 0; i_A < M; i_A++)
            {
            	String[] arr_A = br.readLine().split(" ");
            	for(int j_A = 0; j_A < arr_A.length; j_A++)
            	{
            		A[i_A][j_A] = Integer.parseInt(arr_A[j_A]);
            	}
            }

            int out_ = solve(M, N, A);
            System.out.println(out_);
            
         }

         wr.close();
         br.close();
    }
    static int solve(int M, int N, int[][] A){
       // Write your code here
        int result = 0;
        ArrayList<String> strs = new ArrayList();
        for(int i=0;i<N; ++i) {
            String s = "";
            for (int j=0; j<M;++j) {
                s+=A[i][j];
            }
            strs.add(s);
        }
        int largestLength = 0;
        String[] cmpStrs = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        for (int t_i=0; t_i <= 9; ++t_i) {
            String comparingString = cmpStrs[t_i];
            if (doesExistsInAll(strs, comparingString)) {

            }
        }
        return result;
    }

    static recursiveFuntion() {
        
    }

    static String[] findAllSubs(String fullStr, String key) {
        ArrayList<String> strs = new ArrayList();
        for (String s:fullStr.split(key)) {
            strs.add(key+new String(s.charAt(0)));
        }
        return strs;
    }

    static boolean doesExistsInAll(ArrayList<String> strs, String key) {
        boolean inAll = true;
        for (String str: strs) {
            if (str.indexOf(key) == -1) {
                inAll = false;
            }
        }
        return inAll;
    }
}