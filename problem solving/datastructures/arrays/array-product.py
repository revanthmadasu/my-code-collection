'''
    problem: https://leetcode.com/problems/product-of-array-except-self
    concepts: arrays, math
    performance: 91% runtime, 99.4 memory
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0]*len(nums)
        real_prod = 0 if zero_count else product
        
        return list(map(lambda num: product if num == 0 else real_prod/num, nums))
        