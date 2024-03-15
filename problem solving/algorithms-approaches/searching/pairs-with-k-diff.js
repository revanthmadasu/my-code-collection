'use strict';
// https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the pairs function below.
function Num(num) {
    return {
        num: num,
        checked: false,
        count: 1
    }
}
function pairs(k, arr) {
    let numsMap = {}
    for(let num of arr) {
        if(!numsMap[num]) {
            numsMap[num] = Num(num)
        }
        else{
            numsMap[num].count += 1
        }
    }
    let count = 0
    for(let num in numsMap){
        if(numsMap[num + k]) {
            if ((!numsMap[num].checked) || (!numsMap[num+k].checked)) {
                count += (numsMap[num].count * numsMap[num + k].count)
                // console.log(`pair: num1: ${num}, count1: ${numsMap[num].count}\t\t num2: ${num+k}, count2: ${numsMap[num + k].count}`)
                numsMap[num].checked = true
                numsMap[num+k].checked = true
            }
        }
        if(numsMap[num - k]) {
            if ((!numsMap[num].checked) || (!numsMap[num-k].checked)) {
                count += (numsMap[num].count * numsMap[num - k].count)
                // console.log(`pair: num1: ${num}, count1: ${numsMap[num].count}\t\t num2: ${num+k}, count2: ${numsMap[num - k].count}`)
                numsMap[num].checked = true
                numsMap[num-k].checked = true
            }
        }
    }
    return count
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nk = readLine().split(' ');

    const n = parseInt(nk[0], 10);

    const k = parseInt(nk[1], 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    let result = pairs(k, arr);

    ws.write(result + "\n");

    ws.end();
}
