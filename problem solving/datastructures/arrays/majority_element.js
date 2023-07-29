/**
 * problem: https://leetcode.com/problems/majority-element
 * concepts: arrays, hashtable
 * runtime: 90% memory: 47.6%
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const numsCount = {};
    let maxKey = nums[0];
    nums.forEach(num => {
        if (!numsCount[num]) {
            numsCount[num] = 0;
        }
        numsCount[num] += 1;
        if (numsCount[num] > numsCount[maxKey]) {
            maxKey = num;
        }
    });
    if (numsCount[maxKey] > Math.floor(nums.length/2)) {
        return maxKey;
    }
    return -1;
};