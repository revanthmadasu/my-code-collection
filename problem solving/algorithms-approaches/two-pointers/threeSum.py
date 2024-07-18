'''
    problem: https://leetcode.com/problems/3sum
    concepts: sorting, two pointers, arrays
    performance: 9.51% runtime, 10.09 memory
'''
from typing import List
class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        numOccDict = dict()
        
        for i in range(len(nums)):
            if nums[i] not in numOccDict:
                numOccDict[nums[i]] = 0
            numOccDict[nums[i]] += 1
        keys = sorted(numOccDict.keys())
        # print(f'{numOccDict}')
        for i in range(len(keys)):
            # print(f'keys[i]: {keys[i]}')
            numOccDict[keys[i]] -= 1
            for j in range(i, len(keys)):
                # print(f'keys[j]: {keys[j]}')
                if numOccDict[keys[j]] <= 0:
                    # print(f'j not sufficient for {keys[j]}')
                    continue
                numOccDict[keys[j]] -= 1
                req = -(keys[i] + keys[j])
                # print(f'req is {req}, count: {numOccDict[req] if req in numOccDict else -1}')
                if req in numOccDict and numOccDict[req] > 0:
                    # print(f'{[keys[i], keys[j], req]}')
                    res.add(tuple(sorted([keys[i], keys[j], req])))
                numOccDict[keys[j]] += 1
            numOccDict[keys[i]] += 1
        return res
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res = set()
    #     nums.sort()
    #     numsCount = dict()
    #     n = len(nums)
    #     for num in nums:
    #         numsCount[num] = (numsCount[num] if num in numsCount else 0) + 1
    #     for i in range(n):
    #         cur_num = nums[i]
    #         numsCount[cur_num] -= 1
    #         for j in range(n-1, i, -1):
    #             second_num = nums[j]
    #             numsCount[second_num] -= 1
    #             third_required = (cur_num + second_num) * -1
    #             if (third_required in numsCount) and (numsCount[third_required]):
    #                 res.add(tuple(sorted([cur_num, second_num, third_required])))
    #             numsCount[second_num] += 1
    #         numsCount[cur_num] += 1
    #     return res
