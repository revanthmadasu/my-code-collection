'''
    problem: https://leetcode.com/problems/remove-element
    concepts: arrays
    runtime: 17.6% memory: 37.8%
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res_nums = []
        for num in nums:
            if num != val:
                res_nums.append(num)
        k = len(res_nums)
        for i in range(k):
            nums[i] = res_nums[i]
        return k        