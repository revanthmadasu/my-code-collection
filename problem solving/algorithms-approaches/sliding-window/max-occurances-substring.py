'''
    problem: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring
    concepts: Sliding Window, Hash Table
    performance: 12% runtime, 5% memory
    # todo: write clean code --- IGNORE ---
'''
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        right = minSize-1
        subStringCounts = dict()
        initSubStr = s[left:right+1]
        charCountDict = dict()
        for ch in initSubStr:
            if ch not in charCountDict:
                charCountDict[ch] = 0
            charCountDict[ch] += 1
        maxSubStringRepeatedCount = 0
        if len(charCountDict) <= maxLetters:
            subStringCounts[initSubStr] = 1
        while right < len(s):
            stoppedAt = 0
            # print(f'left: {left}, right: {right}, substr: {s[left:right+1]}, charCounts: {charCountDict}')
            if len(charCountDict) <= maxLetters:
                for ext in range(1, maxSize - minSize + 1):
                    if right + ext >= len(s):
                        break
                    ch = s[right + ext]
                    if ch not in charCountDict: 
                        if len(charCountDict) + 1 > maxLetters:
                            break
                        charCountDict[ch] = 0
                    charCountDict[ch] += 1
                    subStr = s[left:right + ext + 1]
                    if subStr not in subStringCounts:
                        subStringCounts[subStr] = 0
                    # print(f'added 2: {subStr}, charcounts: {charCountDict}')
                    subStringCounts[subStr] += 1
                    maxSubStringRepeatedCount = max(maxSubStringRepeatedCount, subStringCounts[subStr])
                    stoppedAt = ext
            for ext in range(stoppedAt, 0, -1):
                ch = s[right + ext]
                if charCountDict[ch] == 1:
                    del charCountDict[ch]
                else:
                    charCountDict[ch] -= 1
            # print(f'char counts after processing: {charCountDict}')
            if charCountDict[s[left]] == 1:
                del charCountDict[s[left]]
            else:
                charCountDict[s[left]] -= 1
            right += 1
            left += 1
            if right >= len(s):
                break
            if s[right] not in charCountDict:
                charCountDict[s[right]] = 0
            charCountDict[s[right]] += 1
            if len(charCountDict) <= maxLetters:
                if s[left:right+1] not in subStringCounts:
                    subStringCounts[s[left:right+1]] = 0
                subStringCounts[s[left:right+1]] += 1
                # print(f'added 1: {s[left:right+1]}')
                maxSubStringRepeatedCount = max(maxSubStringRepeatedCount, subStringCounts[s[left:right+1]])
        # print(f'substr counts: {subStringCounts}')
        return maxSubStringRepeatedCount