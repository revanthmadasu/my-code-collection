'use strict';
// https://www.hackerrank.com/challenges/luck-balance/problem?h_r=internal-search
const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function luckBalance(k, contests) {
    let maxLuck = 0;
    let unimportantContests = contests.filter(contest => {
        if (!contest[1]) {
            maxLuck+=contest[0]
        }
        return !contest[1];
    });
    let importantContests = contests.filter(contest => !!contest[1])
    .sort((contest1, contest2) => contest2[0] - contest1[0]); 
    const boundary = Math.min(k,importantContests.length);
    for (let i=0; i<boundary; ++i) {
        maxLuck += importantContests[i][0];
    }
    for (let i=boundary; i<importantContests.length; ++i) {
        maxLuck -= importantContests[i][0];
    }
    // console.log(importantContests);
    return maxLuck;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nk = readLine().split(' ');

    const n = parseInt(nk[0], 10);

    const k = parseInt(nk[1], 10);

    let contests = Array(n);

    for (let i = 0; i < n; i++) {
        contests[i] = readLine().split(' ').map(contestsTemp => parseInt(contestsTemp, 10));
    }

    const result = luckBalance(k, contests);

    ws.write(result + '\n');

    ws.end();
}
