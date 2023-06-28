/**
 * problem: https://leetcode.com/problems/string-to-integer-atoi/description/
 * concepts: Strings, regex
 * runtime: 64.2%, memory: 80.6%
 */

/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let myregex = /^(\s)*[-|+]?([0-9]+)/g;
    let matched = s.match(myregex);
    let myNum = parseInt((matched && matched[0] && matched[0].trim() || '0') || '0');
    const [lower, upper] = [Math.pow(-2, 31), Math.pow(2, 31) - 1];
    if (myNum > upper) {
        return upper;
    } else if (myNum < lower) {
        return lower;
    } else {
        return myNum;
    }
};