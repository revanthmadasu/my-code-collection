'''
    Problem: https://leetcode.com/problems/max-consecutive-ones-iii/
    Concepts: Sliding Window
    performance: 81.44% runtime, 7.98% memory
    intuition: segregate continuous sequences of 1's and 0's into tuple and add it into counts array.
    then using sliding window approach, expand right and count 1's till we can flip. 
    when we cannot flip the left pointer moves right and more flips would be available as we are removing the left items.
    when calculating max, try to add the remaining flips to left and right of the window as much as possible
'''
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counts = []
        i = 0
        while i < len(nums):
            oneCount = 0
            while i < len(nums) and nums[i] == 1:
                oneCount += 1
                i += 1
            zeroCount = 0
            while i < len(nums) and nums[i] == 0:
                zeroCount += 1
                i += 1
            counts.append((oneCount, zeroCount))
        left = 0
        right = 1
        remainingFlips = k
        oneCount = counts[0][0]
        maxOneCount = counts[0][0] + min(counts[0][1], remainingFlips)
        # print(f'counts: {counts}')
        while left < right and right < len(counts):
            # oneCount += counts[right][0]
            while counts[right-1][1] > remainingFlips and left < right:
                # print(f'removing {left}')
                oneCount -= ((counts[left][0]+counts[left][1]) if left >= 0 else 0)
                remainingFlips += counts[left][1]
                left += 1
            oneCount += (counts[right][0] + counts[right-1][1])
            remainingFlips -= counts[right-1][1]
            right += 1
            possibleFlipsLeft = min(counts[left-1][1] if left-1  >= 0 else 0, remainingFlips)
            stillRemaining = remainingFlips - possibleFlipsLeft
            possibleFlipsRight = min(stillRemaining, counts[right-1][1])
            curMaxCount = oneCount + possibleFlipsLeft + possibleFlipsRight
            # print(f'counts in window: [{left},{right}): {curMaxCount}')
            maxOneCount = max(maxOneCount, curMaxCount)
        return maxOneCount
