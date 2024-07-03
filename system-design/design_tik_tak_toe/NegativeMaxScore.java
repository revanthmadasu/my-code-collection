package design_tik_tak_toe;
public class NegativeMaxScore implements MaxScore {
    public int operate(int a, int b) {
        return Math.min(a,b);
    }
}