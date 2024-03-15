/**
 * Problem: https://leetcode.com/problems/container-with-most-water/description/
 * Concepts: Arrays, Two Pointers, Greedy
 * Runtime: 16.57%, Memory: 21.6%
 */
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0, right = height.length - 1;
    let maximumArea = 0;
    while (left < right && left < height.length && right > 0) {
        const area = Math.min(height[left], height[right]) * (right - left);
        if (area > maximumArea) {
            maximumArea = area;
        }
        if (height[left] < height[right]) {
            ++left;
        } else {
            --right;
        }
    }
    return maximumArea;
};