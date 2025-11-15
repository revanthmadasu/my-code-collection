'''
    Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
    Concepts: Sliding Window, Hashtable
    performance: 5.02% runtime, 86.72% memory
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        counts = dict()
        def canAllow():
            max_count = 0
            total_count = 0
    
            for ch in counts:
                total_count += counts[ch]
                max_count = max(max_count, counts[ch])
            return total_count - max_count <= k
        max_length = 0
        while r < len(s):
            if s[r] not in counts:
                counts[s[r]] = 0
            counts[s[r]] += 1
            while not canAllow():
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r-l+1)
            r += 1
        return max_length