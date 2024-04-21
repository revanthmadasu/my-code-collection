'''
    Problem: https://leetcode.com/problems/maximum-product-subarray/
    Concepts: Dynamic Programming
    Performance: 89.11% runtime, 86.36% memory
'''
from typing import List
class Solution:
    # dynamic programming approach
    def maxProduct(self, nums: List[int]) -> int:
        negProd = 0
        posProd = 0
        maxProd = 0
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num < 0:
                negProd, posProd = (1 if posProd==0 else posProd) * num, negProd * num
            elif num > 0:
                negProd, posProd = negProd * num, (1 if posProd==0 else posProd) * num
            else:
                negProd, posProd = 0, 0
            maxProd = max(maxProd, posProd)
        return maxProd 
# prefix product, sliding window approach => time limit exceeded
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         prefixProd = []
#         prod = 1
#         for num in nums:
#             prod *= num
#             if prod == 0:
#                 prod = num
#             prefixProd.append(prod)
#         maxProd = max(max(prefixProd), max(nums))
#         # print(f'{prefixProd}')
#         # sliding window approach, prefix product
#         for l in range(len(nums)):
#             for r in range(l+1, len(nums)):
#                 if prefixProd[r] == 0:
#                     break
#                 # print(f'checking {prefixProd[l]} - {prefixProd[r]}')
#                 prod = prefixProd[r]/prefixProd[l] if prefixProd[l] != 0 else prefixProd[r]
#                 maxProd = max(prod, maxProd)
#                 # print(f'max prod is {maxProd}, prod is {prod}')
#         return int(maxProd)