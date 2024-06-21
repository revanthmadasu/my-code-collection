'''
    Problem: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
    Concepts: Sliding Window, Divide and Conquer, Recursion
    performance: 91.58% runtime, 82.82% memory
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        # print(f'received: {s}')
        charCount = dict()
        for ch in s:
            if ch not in charCount:
                charCount[ch] = 0
            charCount[ch] += 1
        left = 0
        windowCharCount = dict()
        maxsize = 0
        for i in range(len(s)):
            ch = s[i]
            if charCount[ch] < k:
                # if current char not possible break window and check the window seperately. remove the window counts
                for windowCh in windowCharCount:
                    charCount[windowCh] -= windowCharCount[windowCh]
                    windowCharCount[windowCh] = 0
                maxsize = max(maxsize, self.longestSubstring(s[left:i], k))
                left = i+1
            else:
                if ch not in windowCharCount:
                    windowCharCount[ch] = 0
                windowCharCount[ch] += 1
        maxsize = max(maxsize, len(s) - left)
        return maxsize