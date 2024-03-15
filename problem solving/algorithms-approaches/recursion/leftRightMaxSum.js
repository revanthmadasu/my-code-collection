/**
 * asked in a assessment
 * concepts: recursion, binary trees
 */
/**
 * 
 * @param {number} arr 
 * @returns string
 */
const solution = (arr) => {
    const {left, right} = recSumCalc(arr, 0);
    if (left > right) {
        return 'Left';
    } else if (right > left) {
        return 'Right';
    } else return '';
};

// return sum of left and right branches as object
const recSumCalc = (arr, k) => {
    const leftInd = 2*(k+1) - 1;
    const rightInd = 2*(k+1);
    let leftSum = 0, rightSum = 0;
    // left element exists in tree
    if (leftInd < arr.length && arr[leftInd] != -1) {
        leftSum = arr[leftInd];
        const {left, right} = recSumCalc(arr, leftInd);
        leftSum += (left + right);
    }
    if (rightInd < arr.length && arr[rightInd] != -1) {
        rightSum = arr[rightInd];
//         console.log(`Setting right sum to ${rightSum}`);
        const {left, right} = recSumCalc(arr, rightInd);
        rightSum += (left + right);
    }
//     console.log(`k = ${k} left sum: ${leftSum}, right sum: ${rightSum}`);
    return {left: leftSum, right: rightSum};
}
