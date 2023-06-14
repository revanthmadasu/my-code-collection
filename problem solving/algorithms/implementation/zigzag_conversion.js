/**
 * problem: https://leetcode.com/problems/zigzag-conversion
 * concepts: string, arithmetics, patterns
 * runtime: 24.5%, memory = 17.6%
 */

/*
    Approach: 
        Pattern:
        0     6      12
        1   5 7   11 13
        2 4   8 10   14
        3     9      15

        Repetitive joint
        0
        1   5 
        2 4
        3 
        join wise search for indices and assigning these indices to row lists
        maintain row wise lists
        create list of indexes for first row => i = prev_i + (2*(numRows - 1))
        for each item in this row, calculate indices for 2nd to last rows
        last row has single item which is first_i + numRows - 1
        middle rows have 2 elements in each joint
            first occuring is first_i + row_index
            second occuring is first_i + (2* (numRows - 1) - rowIndex)
        then merge all these lists of indexes
        obtain string from indexes using original string
*/
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows == 1) {
        return s;
    }
    const n = s.length;
    const fullJointLength = numRows + numRows - 2;
    const numJoints = Math.ceil(n/fullJointLength);
    console.log(`fullJointLength: ${fullJointLength}\nnumJoints: ${numJoints}`);
    const firstRows = (() => {
        const rows = [0];
        let index = 0;
        for (let i=1; i<numJoints; ++i) {
            index = index + 2 * (numRows - 1);
            if (index >= n) {
                break;
            }
            rows.push(index);
        }
        return rows;
    })();
    console.log(`firstRows: ${firstRows}`);
    let restRows = (() => {
        const rows = [];
        for (let i=1; i<numRows; ++i) {
            rows.push([]);
        }
        return rows;
    })();
    console.log(`restRows: ${restRows}`);
    // assigning indices row wise
    for (let jointStartIndex of firstRows) {
        for (let row_i=1; row_i<numRows; ++row_i) {
            const f_occ_index = jointStartIndex + row_i;
            if (f_occ_index >= n) {
                break;
            }
            // console.log(`row id: ${row_i}`);
            restRows[row_i-1].push(f_occ_index);
            // middle rows
            if (row_i !== numRows-1) {
                const s_occ_index = jointStartIndex + (2*(numRows - 1) - row_i);
                if (s_occ_index >= n) {
                    continue;
                }
                restRows[row_i-1].push(s_occ_index);
            }
        }
    }
    console.log(`first rows: ${firstRows}\n restrows: ${restRows}`);
    return [firstRows, ...restRows].reduce((row1, row2) => {
        if (row1 && row1.push) {
            row1.push(...row2);
        } 
        return row1;
    }, []).map(i => s[i]).join("");
};

// console.log(convert("PAYPALISHIRING", 3));
console.log(convert("ABC", 3));

// console.log(convert("A", 1));