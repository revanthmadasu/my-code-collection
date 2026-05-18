'''
    Problem: https://leetcode.com/problems/minimum-window-substring/
    concepts: Sliding Window, Two Pointers, Hash Table, String
    performance: 78.91% runtime, 66.14% memory
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sCharCountsMap = dict()
        tCharCountsMap = dict()
        charCountWindowMap = dict()
        def countCharsIntoMap(string, map):
            for char in string:
                if char not in map:
                    map[char] = 0
                map[char] += 1
        def windowContains():
            for ch in tCharCountsMap:
                if ch not in charCountWindowMap or charCountWindowMap[ch] < tCharCountsMap[ch]:
                    return False
            return True
        # countCharsIntoMap(s, sCharCountsMap)
        countCharsIntoMap(t, tCharCountsMap)
        l,r = 0, 0
        charCountWindowMap[s[l]] = 1
        minWindowString = ""

        while l <= r and r < len(s):
            if windowContains():
                # print(f'found possible between - l: {l}, r: {r}, string: {s[l:r+1]}')
                if minWindowString == "" or len(minWindowString) > r-l+1:
                    minWindowString = s[l:r+1]
                charCountWindowMap[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < len(s):
                    if s[r] not in charCountWindowMap:
                        charCountWindowMap[s[r]] = 0
                    charCountWindowMap[s[r]] += 1
        return minWindowString
        