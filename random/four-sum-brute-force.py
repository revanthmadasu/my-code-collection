'''
    problem: https://leetcode.com/problems/4sum/
    concepts: Bruteforce
    #incomplete - testcases failing
    #todo: complete it
'''
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Recursive search aproach - 233/294
        res = set()
        numsCount = dict()
        for num in nums:
            if num not in numsCount:
                numsCount[num] = 0
            numsCount[num] += 1
        uniqueNums = list(numsCount.keys())
        print(numsCount)
        def recursiveSearch(start, added):
            # print(f'cur added: {added}')
            if start >= len(uniqueNums):
                return
            remaining = 4 - len(added)
            curNumCount = numsCount[uniqueNums[start]]
            numReps = min(curNumCount, remaining)
            for numRep in range(1, numReps+1):
                # print(f'adding {uniqueNums[start]} {numRep} times')
                curAdded = added + [uniqueNums[start]] * numRep
                addedSum = sum(curAdded)
                if len(curAdded) == 4:
                    if addedSum == target:
                        res.add(tuple(curAdded))
                else:
                    recursiveSearch(start+1, curAdded)
            recursiveSearch(start+1, added)
            return
        recursiveSearch(0, [])
        return [list(item) for item in list(res)]
        # Brute force approach - 288/294
        # for i in range(len(nums)-3):
        #     num1 = nums[i]
        #     for j in range(i+1, len(nums)-2):
        #         num2 = nums[j]
        #         for k in range(j+1, len(nums)-1):
        #             num3 = nums[k]
        #             for l in range(k+1, len(nums)):
        #                 num4 = nums[l]
        #                 # print(f'{i}, {j}, {k}, {l} => {num1}, {num2}, {num3}, {num4}')
        #                 if num1+num2+num3+num4 == target:
        #                     res.add(tuple(sorted([num1, num2, num3, num4])))
        # return [list(item) for item in list(res)]