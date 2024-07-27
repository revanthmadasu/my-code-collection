package design_tik_tak_toe;
import java.util.Random;

interface MaxScore {
    public int operate(int a, int b);
}

class NegativeMaxScore implements MaxScore {
    public int operate(int a, int b) {
        return Math.min(a,b);
    }
}

class PositiveMaxScore implements MaxScore {
    public int operate(int a, int b) {
        return Math.max(a,b);
    }
}

public class TikTakToe {
    private final int board[][];
    private int movesMade = 0;
    public boolean isGameOver = false;
    TikTakToe() {
        this.board = new int[3][3];

    }
    /*
     * @param row is the move's row
     * @param col is move's column
     * @param player is 1 or -1 representing player
     * @return 1 if player 1 is winner, -1 if player -1 is winner, 0 if no winner for move
     */
    public int move(int row, int col, int player) throws IllegalArgumentException {
        if (row < 0 || row > 2 || col < 0 || col > 2) {
            throw new IllegalArgumentException("Out of board");
        }
        if (player != 1 && player != -1) {
            throw new IllegalArgumentException("Invalid player");
        }
        if (this.board[row][col] != 0) {
            throw new IllegalArgumentException("Move already occupied");
        }
        MaxScore scoreCalc = player > 0 ? new PositiveMaxScore() : new NegativeMaxScore();
        this.board[row][col] = player +
        ((row-1 >= 0) ? scoreCalc.operate(0, board[row-1][col]) : 0) +
        ((row+1 < 3) ? scoreCalc.operate(0, board[row+1][col]) : 0) +
        ((col+1 < 3) ? scoreCalc.operate(0, board[row][col+1]) : 0) +
        ((col-1 >= 0) ? scoreCalc.operate(0, board[row][col-1]) : 0) +
        ((col+1 < 3 && row-1 >= 0) ? scoreCalc.operate(0, board[row-1][col+1]) : 0) +
        ((col+1 < 3 && row+1 >= 0) ? scoreCalc.operate(0, board[row+1][col+1]) : 0) +
        ((col-1 < 3 && row-1 >= 0) ? scoreCalc.operate(0, board[row-1][col-1]) : 0) +
        ((col-1 < 3 && row+1 >= 0) ? scoreCalc.operate(0, board[row+1][col-1]) : 0);
        this.display();
        ++this.movesMade;
        int winner = Math.abs(this.board[row][col]) >= 3 ? player: 0;
        this.isGameOver = Math.abs(winner) != 0 || this.movesMade >= 9;
        return winner;
    }
    public void display() {
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; ++col) {
                System.out.print(this.board[row][col] == 0 ? "_ " : (this.board[row][col] > 1 ? "X " : "O "));
            }
            System.out.println();
        }
    }

    public static void main(String args[]) {
        TikTakToe game = new TikTakToe();
        int curPlayer = 1;
        Random random = new Random();
        while (game.isGameOver) {
            int row = random.nextInt(3);
            int col = random.nextInt(3);
            try {
                int winner = game.move(row, col, curPlayer);
                if (winner == 0) {
                    curPlayer = -curPlayer;
                } else {
                    System.out.println("Player" + (curPlayer == -1 ? "X" : "O") + " wins");
                }
            } catch (IllegalArgumentException e) {

            }
        }
    }
}
