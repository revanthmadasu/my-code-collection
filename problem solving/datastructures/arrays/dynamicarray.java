import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Complete the dynamicArray function below.
    static List<Integer> dynamicArray(int n, List<List<Integer>> queries) {
        ArrayList<Integer> result=new ArrayList<Integer>();
        ArrayList<Integer>[] sequences=new ArrayList[n];
        for(int i=0;i<n;++i)
            sequences[i]=new ArrayList();
        int lastAnswer=0;
        int q=queries.size();

        for(int i=0;i<q;++i)
        {
            List<Integer> iq=queries.get(i);
            int ch=iq.get(0);
            int x=iq.get(1);
            int y=iq.get(2);
            int seqIndex=(x^lastAnswer)%n;
            if(ch==1)
            {
                sequences[seqIndex].add(y);
            }
            else if(ch==2)
            {
               // System.out.println(y);
                lastAnswer=sequences[seqIndex]
                .get(y%sequences[seqIndex].size());
                result.add(lastAnswer);
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nq = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(nq[0]);

        int q = Integer.parseInt(nq[1]);

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, q).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Integer> result = dynamicArray(n, queries);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}

