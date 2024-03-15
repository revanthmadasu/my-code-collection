# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.myBfs(nums, target, 0, n-1)
    def myBfs(self, nums, target, least, top):
        mid = int((least + top)/2)
        if nums[mid] == target:
            return mid
        elif least == top:
            return least if nums[least] > target else least+1
        elif nums[mid] > target:
            return self.myBfs(nums, target, least, mid)
        else:
            return self.myBfs(nums, target, mid+1, top)