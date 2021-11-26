# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        for i in range(k):
            nums.insert(0,nums.pop())
obj = Solution()
nums = [1,2]
k = 2
obj.rotate(nums,k)
print(nums)
