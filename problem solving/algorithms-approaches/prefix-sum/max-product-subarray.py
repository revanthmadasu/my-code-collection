'''
    Problem: https://leetcode.com/problems/maximum-product-subarray/
    Concepts: Prefix Sum
    #incomplete - time limit exceeded
    #todo - complete it - try dynamic programming
'''
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixProd = []
        prod = 1
        for num in nums:
            prod *= num
            if prod == 0:
                prod = num
            prefixProd.append(prod)
        maxProd = max(max(prefixProd), max(nums))
        # print(f'{prefixProd}')
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if prefixProd[r] == 0:
                    break
                # print(f'checking {prefixProd[l]} - {prefixProd[r]}')
                prod = prefixProd[r]/prefixProd[l] if prefixProd[l] != 0 else prefixProd[r]
                maxProd = max(prod, maxProd)
                # print(f'max prod is {maxProd}, prod is {prod}')
        return int(maxProd)