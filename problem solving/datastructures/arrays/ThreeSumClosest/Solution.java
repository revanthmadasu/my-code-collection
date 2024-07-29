/*
    problem: https://leetcode.com/problems/3sum-closest/
    concepts: Arrays, Sorting, Two Pointers
    performance: 67.61% runtime, 62.18% memory
    #revise - searched solution
*/
package ThreeSumClosest;
import java.util.Arrays;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestTarget = (int) Double.POSITIVE_INFINITY;
        for (int i=0; i<nums.length; ++i) {
            int start = i + 1;
            int end = nums.length - 1;
            while(start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if (sum == target) {
                    return sum;
                }
                if (Math.abs(sum - target) < Math.abs(closestTarget - target)) {
                    closestTarget = sum;
                }
                if (sum > target) {
                    end -= 1;
                } else {
                    start += 1;
                }
            }
        }
        return closestTarget;
    }
}