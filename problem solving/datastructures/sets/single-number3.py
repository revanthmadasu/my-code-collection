'''
    problem: https://leetcode.com/problems/single-number-iii/
    concepts: Sets
    performance: 89.89% runtime, 41.53% memory
'''
from typing import List
# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         nums_set = set()
#         for num in nums:
#             nums_set.remove(num) if num in nums_set else nums_set.add(num)
#         return list(nums_set)
import math

class Solution:
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        def matches(num, bitPos):
            binNum = bin(num)[2:]
            return len(binNum) > bitPos and binNum[bitPos] == '1'
        def getBitPos(num):
            return int(math.log(num,2))
        xor = 0
        for num in nums:
            xor = xor ^ num
        print(f'xor is {xor}')
        bitPos = getBitPos(xor)
        doesMatch = 0
        doesNotMatch = 0
        for num in nums:
            if matches(num, bitPos):
                doesMatch = doesMatch ^ num
            else:
                doesNotMatch = doesNotMatch ^ num
        return [doesMatch, doesNotMatch]
    
sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5]))