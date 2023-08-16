'''
    problem: https://leetcode.com/problems/summary-ranges
    concepts: arrays, range
    performance: 42.85% runtime, 95.11% memory
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        prevNum = nums[0]
        seq_start = nums[0]
        ranges_list = []
        def addToRangeList(seq_start, prevNum):
            if seq_start == prevNum:
                ranges_list.append(f'{seq_start}')
            else:
                ranges_list.append(f'{seq_start}->{prevNum}')
        for num in nums:
            if num - prevNum == 1 or num - prevNum == 0:
                prevNum = num
            else:
                addToRangeList(seq_start, prevNum)
                seq_start = num
                prevNum = num
        addToRangeList(seq_start, prevNum)

        return ranges_list