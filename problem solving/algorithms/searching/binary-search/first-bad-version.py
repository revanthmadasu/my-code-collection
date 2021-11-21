# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
# URL https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        last = n-1
        result = self.myBfs(0,n)
        return result
        
    def myBfs(self, least, top):
        if top - least <= 1:
            if isBadVersion(least):
                return least
            elif isBadVersion(top):
                return top
        mid = int((least + top)/2)
        if isBadVersion(mid):
            return self.myBfs(least, mid)
        else:
            return self.myBfs(mid+1, top)