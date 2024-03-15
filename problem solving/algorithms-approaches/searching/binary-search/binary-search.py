# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = int(n/2)
        if target == nums[mid]:
            return mid
        if n == 1:
            return -1
        if target < nums[mid]:
            return self.search(nums[0:mid], target)
        else:
            res = self.search(nums[mid:], target)
            return -1 if res == -1 else mid + res