/**
 * https://leetcode.com/problems/01-matrix/description/
 * Concepts: BFS, Dynamic Programming, Matrices
 * Speed: 9.6% Memory: 6.9%
 * Optimization required
 */
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function(mat) {
    // m rows, n columns
    const m = mat.length, n = mat[0].length;
    let distMat = [];
    let zeroIndexes = [];
    // populating res matrix - initially -1 distance
    for (let i=0; i<m; ++i) {
        let row = [];
        for (let j=0; j<n; ++j) {
            row.push(Number.POSITIVE_INFINITY);
            if (mat[i][j] === 0) {
                zeroIndexes.push([i,j])
            }
        }
        distMat.push(row);
    }
    // console.log(`m is ${m}, n is ${n}`);
    // console.log(`Dist matrix is ${distMat}`);
    let queue = [...zeroIndexes];
    let currentValue = 0;
    while (queue.length) {
        let newQueue = [];
        for(let queueItem of queue) {
            let [i, j] = queueItem;
            // console.log(`Queue item is ${queueItem}. Current: ${distMat[i][j]}, Setting: ${currentValue}`);
            if (distMat[i][j] > currentValue) {
                distMat[i][j] = currentValue;
                console.log(`${[[i+1, j], [i-1, j], [i, j+1], [i, j-1]]}`);
                [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                    .filter(pair => pair[0] >=0 && pair[0] < m && pair[1] >= 0 && pair[1] < n)
                    .forEach(pair => {
                        // console.log(`Pushing ${pair}`);
                        newQueue.push(pair)
                    });
            }
        }
        ++currentValue;
        // console.log(`new queue is ${newQueue}`);
        queue = newQueue;
    }
    return distMat;
};