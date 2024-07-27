package design_tik_tak_toe;

public class PositiveMaxScore implements MaxScore {
    public int operate(int a, int b) {
        return Math.max(a,b);
    }
}
