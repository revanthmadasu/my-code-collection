/**
 * Problem: https://leetcode.com/problems/valid-sudoku
 * concepts: matrices, maps, arrays
 */
function isValidSudoku(board: string[][]): boolean {
    const colsMap = {};
    const rowsMap = {};
    const innerSquaresMap = {};
    const getBoxIndex = (i: number, j: number) => {
        const boxI = Math.floor(i/3);
        const boxJ = Math.floor(j/3);
        return (boxI*3) + boxJ; 
    };
    const isEmpty = (key) => key === '.';
    for (let i=0; i<board.length; ++i) {
        colsMap[i] = {};
        rowsMap[i] = {};
        innerSquaresMap[i] = {};
    }
    for (let i=0; i<board.length; ++i) {
        const row = board[i];
        for (let j=0; j<row.length; ++j) {
            const val = row[j];
            if (!isEmpty(val)) {
                // rows check
                if (rowsMap[i][val]) {
                    return false;
                } else {
                    rowsMap[i][val] = true;
                }
                // columns check
                if (colsMap[j][val]) {
                    return false;
                } else {
                    colsMap[j][val] = true;
                }
                // inner box check
                const boxIndex = getBoxIndex(i,j);
                if (innerSquaresMap[boxIndex][val]) {
                    return false;
                } else {
                    innerSquaresMap[boxIndex][val] = true;
                }
            }
        }
    }

    return true;
};

const board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
];

isValidSudoku(board);
