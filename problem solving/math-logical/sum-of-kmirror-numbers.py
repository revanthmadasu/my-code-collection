'''
    Problem: https://leetcode.com/problems/sum-of-k-mirror-numbers/
    Concepts: Palindromes, Base conversion, Math
    Performance: 10% runtime, 65% memory
'''
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def getBaseK(num):
            kBaseNum = ""
            if num < k:
                return str(num)
            while num >= k:
                kBaseNum = str(num%k) + kBaseNum
                num = num//k
            kBaseNum = str(num) + kBaseNum
            # print(f'kbase for {fNum}  is {kBaseNum}')
            return kBaseNum
        def isPalindrome(s):
            return s == s[::-1]
        def getNextPalindrome(s):
            if not s:
                return "1"
            subStr = s[:math.ceil(len(s)/2)]
            pos = len(subStr)-1
            while subStr[pos] == '9' and pos >= 0:
                subStr = subStr[:pos] + '0' + subStr[pos+1:]
                pos -= 1
            if pos == -1:
                return '1' + '0' * (len(s) - 1) + '1'
            else:
                num = int(subStr[pos])
                newSubStr = subStr[:pos] + str(num+1) + subStr[pos+1:]
                return (newSubStr + newSubStr[::-1]) if len(s)%2 == 0 else (newSubStr + newSubStr[:-1][::-1])
    

        palindromeSum = 0
        count = 0
        prevPalindrome = ""
        while count != n:
            palindrome = getNextPalindrome(prevPalindrome)
            num = int(palindrome)
            # print(f'checking for {num}')
            if isPalindrome(getBaseK(num)):
                # print(f'adding {num}')
                palindromeSum += num
                count += 1
            prevPalindrome = palindrome
        return palindromeSum
        