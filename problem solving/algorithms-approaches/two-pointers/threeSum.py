'''
    problem: https://leetcode.com/problems/3sum
    concepts: sorting, two pointers, arrays
    performance: 5.01% runtime, 84.37 memory
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        numsCount = dict()
        n = len(nums)
        for num in nums:
            numsCount[num] = (numsCount[num] if num in numsCount else 0) + 1
        for i in range(n):
            cur_num = nums[i]
            numsCount[cur_num] -= 1
            for j in range(n-1, i, -1):
                second_num = nums[j]
                numsCount[second_num] -= 1
                third_required = (cur_num + second_num) * -1
                if (third_required in numsCount) and (numsCount[third_required]):
                    res.add(tuple(sorted([cur_num, second_num, third_required])))
                numsCount[second_num] += 1
            numsCount[cur_num] += 1
        return res
