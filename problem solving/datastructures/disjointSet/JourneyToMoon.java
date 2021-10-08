/**
    https://www.hackerrank.com/challenges/journey-to-the-moon/problem
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    
        static long journeyToMoon(int n, int[][] astronautPairs) {
        int disjointSet[]=new int[n];
        // int astronautIds[]=new int[n];
        for(int i=0;i<n;++i)
            disjointSet[i]=i;
        for(int []pair:astronautPairs) {
            int v1=pair[0],v2=pair[1];
            if(disjointSet[v1]>disjointSet[v2]) {
                merge(disjointSet,disjointSet[v1],disjointSet[v2]);
            }
            else if(disjointSet[v2]>disjointSet[v1]) {
                merge(disjointSet,disjointSet[v2],disjointSet[v1]);
            }
        }
        int count[]=new int[n];
        for(int i=0;i<n;++i){
            count[i]=0;
        }
        for(int i=0;i<n;++i) {
            ++count[disjointSet[i]];
        }
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i:count) {
            if(i!=0)
                list.add(i);
        }
        Integer countrySizes[]=new Integer[list.size()];
        countrySizes=list.toArray(countrySizes);
        int tempArr[]=new int[countrySizes.length];
        int sum=0;
        for(int i=countrySizes.length-1;i>0;--i) {
            sum+=countrySizes[i];
            tempArr[i]=sum;
        }
        long sum1=0;
        for(int i=0;i<countrySizes.length-1;++i) {
            sum1+=(countrySizes[i]*tempArr[i+1]);
        }
        return sum1;
    }
    
    static void merge(int []disjointSet,int parent,int child) {
        for(int i=0;i<disjointSet.length;++i) {
            if(disjointSet[i]==child)
                disjointSet[i]=parent;
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] np = scanner.nextLine().split(" ");

        int n = Integer.parseInt(np[0]);

        int p = Integer.parseInt(np[1]);

        int[][] astronaut = new int[p][2];

        for (int i = 0; i < p; i++) {
            String[] astronautRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 2; j++) {
                int astronautItem = Integer.parseInt(astronautRowItems[j]);
                astronaut[i][j] = astronautItem;
            }
        }

        long result = journeyToMoon(n, astronaut);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}