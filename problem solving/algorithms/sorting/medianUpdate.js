/*
    https://www.hackerrank.com/challenges/median/problem
    using sorting and little dynamic programming
*/
function processData(input) {
    //Enter your code here
    let inps = input.split('\n')
    let q = parseInt(inps[0])
    let sortedNums = []
    let medianIndex = -1;
    let getMedian = () => {
        let median = 0;
        if (!sortedNums.length) {
            return "Wrong!"
        }
        let middle = parseInt(sortedNums.length/2);
        // console.log(`Getting Median-- sorted list:${sortedNums}, Middle = ${middle}`);
        if (sortedNums.length % 2 === 0) {
            median = (sortedNums[middle] + sortedNums[middle-1])/2;
        } else {
            median = sortedNums[middle]
        }
        return median;
    };
    
    let insertIntoList = num => {
        let prevIndex = -1;
        let start = 0, end = sortedNums.length;
        if (sortedNums.length > 10000) {
            let startUnset = true;
            for (let i=0; i<sortedNums.length; i+=100) {
                if (startUnset) {
                    if (sortedNums[i] > num) {
                        startUnset = false;
                        end = i;
                    } else {  
                        start = i;
                    }
                } else {
                    break;
                }
            }
        }
        for (let i=start; i< end; ++i) {
            if (num < sortedNums[i]) {
                break;
            }
            prevIndex = i;
        }
        sortedNums.splice(prevIndex + 1, 0, num);
        // console.log(`Inserting Number -- sorted list:${sortedNums}, Number = ${num}`);
        return getMedian();
    };
    
    let removeFromList = (num) => {
        const index = sortedNums.findIndex(item => item === num);
        if (index === -1) {
            return "Wrong!"
        }
        sortedNums.splice(index,1);
        // console.log(`Removing Number -- sorted list:${sortedNums}, Number = ${num}, Index = ${index}`);
        return getMedian();
    }
    for (let i=1; i<q+1; ++i) {
        let splitted = inps[i].split(' ')
        let operation = splitted[0];
        let num = parseInt(splitted[1]);
        // console.log(`Operation ${operation}, number ${num}`)
        if (operation === 'a') {
            console.log(insertIntoList(num));
        } else if (operation === 'r') {
            console.log(removeFromList(num));
        }
    }
    // console.log(input.split('\n'))
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
