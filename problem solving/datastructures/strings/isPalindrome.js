/**
 * problem: https://leetcode.com/problems/palindrome-number
 * concepts: string, number to string casting
 * runtime: 42.38% memory: 74.59%
 */
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let string_x = x+"";
    let reverse_x = string_x.split('').reverse().join("");
    return string_x === reverse_x;
};