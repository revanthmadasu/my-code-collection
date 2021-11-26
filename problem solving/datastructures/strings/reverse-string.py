# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        mid=int(n/2)
        for i in range(mid):
            s[i],s[n-1-i] = s[n-1-i],s[i]
