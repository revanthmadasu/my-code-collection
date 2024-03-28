'''
    problem: https://leetcode.com/problems/sliding-window-maximum/
    concepts: Sliding Window, Sorting
    #incomplete - 37/51 testcases passes - timeout error
    #todo: complete it - use binary search to find position
'''
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        slidingWindow = nums[:k]
        slidingWindow.sort()
        maxItems = [slidingWindow[k-1]]
        for i in range(1, len(nums)-k+1):
            # print(f'bf: {slidingWindow}')
            slidingWindow.remove(nums[i-1])
            kthNum = nums[i+k-1]
            if kthNum >= slidingWindow[len(slidingWindow)-1]:
                slidingWindow.append(kthNum)
                # print('appended num')
            else:
                for slidingIndex in range(k-1):
                    if kthNum < slidingWindow[slidingIndex]:
                        slidingWindow.insert(slidingIndex, kthNum)
                        # print('inserted num')
                        break
            maxItems.append(slidingWindow[len(slidingWindow)-1])
            # print(f'af: {slidingWindow}')

        return maxItems