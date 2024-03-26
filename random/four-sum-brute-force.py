'''
    problem: https://leetcode.com/problems/4sum/
    concepts: Bruteforce
    #experiment - worst implementation
    #todo: use hashtable, recursion
'''
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-3):
            num1 = nums[i]
            for j in range(i+1, len(nums)-2):
                num2 = nums[j]
                for k in range(j+1, len(nums)-1):
                    num3 = nums[k]
                    for l in range(k+1, len(nums)):
                        num4 = nums[l]
                        # print(f'{i}, {j}, {k}, {l} => {num1}, {num2}, {num3}, {num4}')
                        if num1+num2+num3+num4 == target:
                            res.add(tuple(sorted([num1, num2, num3, num4])))
        return [list(item) for item in list(res)]