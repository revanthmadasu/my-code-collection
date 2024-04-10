'''
    Problem: https://leetcode.com/problems/first-bad-version
    Concepts: Searching, Binary Search
    performance: 29.64% runtime, 64.68% memory
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
# URL https://leetcode.com/problems/first-bad-version/
class Solution:
    # iterative binary search
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right) // 2
            isBad = isBadVersion(mid)
            if isBad:
                right = mid-1
                if not isBadVersion(right):
                    return mid
            else:
                left = mid+1
        return left
    # recursive binary search - performance: 59.27% runtime, 100% memory
    # def firstBadVersion(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     last = n-1
    #     result = self.myBfs(0,n)
    #     return result
        
    # def myBfs(self, least, top):
    #     if top - least <= 1:
    #         if isBadVersion(least):
    #             return least
    #         elif isBadVersion(top):
    #             return top
    #     mid = int((least + top)/2)
    #     if isBadVersion(mid):
    #         return self.myBfs(least, mid)
    #     else:
    #         return self.myBfs(mid+1, top)