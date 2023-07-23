'''
    problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array
    concepts: arrays, two pointers
    runtime: 32.33% memory: 58.8%
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)    
        p1 , p2 = (0, 0)
        k = 0
        if not n:
            return 0
        while p2 < n:
            val = nums[p2]
            while p2 < n and nums[p2] == val:
                p2 += 1
            nums[p1] = val
            p1+=1
        return p1