
/**
 * asked in Wadhwani AI
 * chain of o's for which starting o is in outermost row/column should be chnaged to 'x'
 */


const matrix = [['x','x','o','x'],
                ['x','o','x','o'],
                ['o','x','x','o']];
/* result shoud be [["x","x","x","x"],
                    ["x","o","x","x"],
                    ["x","x","x","x"]] */
const queue=[];// {row:0, col:0}
const rowsLength = matrix.length;
const colsLength = matrix[0].length;
for(let i=0;i<colsLength; ++i) {
    if (matrix[0][i] == 'o') {
        queue.push({row: 0, col: i})
    }
}

for(let i=0;i<colsLength; ++i) {
    if (matrix[rowsLength - 1][i] == 'o') {
        queue.push({row: rowsLength - 1, col: i})
    }
}

for(let i=0;i<rowsLength; ++i) {
    if (matrix[i][0] == 'o') {
        queue.push({row: i, col: 0})
    }
}

for(let i=0;i<rowsLength; ++i) {
    if (matrix[i][colsLength - 1] == 'o') {
        queue.push({row: i, col: colsLength - 1})
    }
}

console.log(queue);

while(queue.length) {
    const queueItem = queue[0];
    const rowPos = queueItem.row;
    const colPos = queueItem.col;
    if (matrix[queueItem.row][queueItem.col] === 'o') {
        matrix[rowPos][colPos] = 'x';
    }
    // if (rowPos > 0 && colPos > 0) {

    // }
    if ((rowPos+1) < rowsLength && matrix[rowPos + 1][colPos] === 'o') {
        queue.push({row: rowPos + 1, col: colPos});
    }
    if ((rowPos - 1) > 0 && matrix[rowPos - 1][colPos] === 'o') {
        queue.push({row: rowPos - 1, col: colPos});
    }
    if (matrix[rowPos][colPos + 1] === 'o') {
        queue.push({row: rowPos, col: colPos + 1});
    }
    if (matrix[rowPos][colPos - 1] === 'o') {
        queue.push({row: rowPos + 1, col: colPos - 1});
    }
    queue.splice(0,1);
}

console.log(matrix);