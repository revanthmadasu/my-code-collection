'''
    problem: https://leetcode.com/problems/tuple-with-same-product/
    concepts: Hashtable
    performance: 5.06 runtime, 7.60 memory
    #todo: improve performance
'''
from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prodsMap = dict()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in prodsMap:
                    prodsMap[prod] = []
                prodsMap[prod].append((i, j))
        res = 0
        for tuples_list in prodsMap.values():
            if len(tuples_list) > 1:
                combs = len(tuples_list) * (len(tuples_list)-1)
                res += (combs*4)
        return res
