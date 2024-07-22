package random;
class ScorePercentage {
    public static void main(String args[]) {
        int scores[] = {76,56,86,37,49};
        double percent = calculatePercentage(scores);
        System.out.println(percent);
    }

    // <return type> <method name>(<arguments>)
    static double calculatePercentage(int[] scores) {
        int allTotal = scores.length * 100;
        int curTotal = 0;
        for (int i=0; i < scores.length; i++) {
            curTotal += scores[i];
        }
        System.out.println("Score is " + curTotal);
        return ((double)curTotal/allTotal) * 100;
    }
}
