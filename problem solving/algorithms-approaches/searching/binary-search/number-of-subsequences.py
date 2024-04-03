'''
    problem: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
    concepts: Binary Search, Sorting, Array
    #incomplete: 61/63 testcases passed - timeout
    #todo: complete it
'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        allPossibleCounts = 2**len(nums) - 1
        reduceCount = 0
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            # print(f'checking {i}')
            j = i
            r = 0
            start = 0
            end = i
            while end - start > 1:
                mid = (start + end)//2
                if nums[mid] + nums[i] > target:
                    end = mid
                else:
                    start = mid
            maxIndex = None
            if nums[start] + nums[i] > target:
                maxIndex = start
            else:
                if nums[end] + nums[i] > target:
                    maxIndex = end
                else:
                    maxIndex = -1
            # print(f'maxIndex: {maxIndex}')
            r = i - maxIndex + 1
            
            # while j >= 0 and min([nums[i], nums[j]]) + max([nums[i], nums[j]]) > target:
            #     r += 1
            #     j -= 1
            if maxIndex != -1 and r >= 1:
                # print(f'reducing {2**(r-1)}')
                reduceCount += (2**(r-1))
        return (allPossibleCounts - reduceCount) % 1000000007