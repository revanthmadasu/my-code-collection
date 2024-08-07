'''
    problem: https://leetcode.com/problems/longest-palindromic-substring/description
    concepts: strings, palindromes
    runtime: 46.60%, memory: 84.55%
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = ""
        for i in range(len(s)):
            left = right = i
            palindromeLen = 1
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
                palindromeLen += 2
            if palindromeLen > len(maxPalindrome):
                maxPalindrome = s[left: right+1]
        for i in range(len(s)-1):
            left, right = i, i+1
            if s[left] == s[right]:
                palindromeLen = 2
                while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                    palindromeLen += 2
                if palindromeLen > len(maxPalindrome):
                    maxPalindrome = s[left: right+1]
        return maxPalindrome
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
            Approach: 
                1) Maintain a list of palindromes - initially it will be all individual characters in string grouped by character continuously
                    Eg: aababaa: aa,b,a,b,aa
                    Represent these by start and end index as tuples
                2) expand these groups sideways to check if they are palindromes. do it iteratively breadth wise.
                3) end the loop if it becomes empty or length or any palindrome equals string length
        '''
        palindromes = []
        i = 0
        n = len(s)
        max_pal = (-1, -1, 0)
        def checkAddMax(_pal):
            nonlocal max_pal
            # print(f'checking {_pal} with {max_pal}')
            if _pal[2] > max_pal[2]:
                max_pal = _pal
        while i != n:
            j = i
            l = 0
            while j < n and j >= 0 and s[j] == s[i]:
                j = j+1
                l = l+1
            pal = (i, j-1 ,l)
            checkAddMax(pal)
            palindromes.append(pal)
            i = i+1
        while len(palindromes) != 0 and max_pal[2] != n:
            updating_pals = []
            for pal in palindromes:
                i, j, l = pal
                if i-1 < 0 or j+1 >= n:
                    checkAddMax(pal)
                elif s[i-1] != s[j+1]:
                    checkAddMax(pal)
                else:
                    updating_pals.append((i-1, j+1, l+2))
            palindromes = updating_pals
        # print(max_pal)
        return s[max_pal[0]:max_pal[1] + 1]
        