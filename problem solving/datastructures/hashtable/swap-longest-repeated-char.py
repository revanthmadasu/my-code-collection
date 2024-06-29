'''
    Problem: https://leetcode.com/problems/swap-for-longest-repeated-character-substring
    Concepts: Hashtable
    performance: 43.72% runtime, 28.74% memory
'''
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        countsSeq = []
        i = 1
        count = 1
        charCount = dict()
        charCount[text[0]] = 1
        while i < len(text):
            if text[i] not in charCount:
                charCount[text[i]] = 0
            charCount[text[i]] += 1
            if text[i-1] != text[i]:
                countsSeq.append((text[i-1], count))
                count = 1
            else:
                count += 1
            i += 1
        if count:
            countsSeq.append((text[-1], count))
        # print(f'seqs: {countsSeq}')
        maxSeqCount = 1
        for i, seq in enumerate(countsSeq):
            maxSeqCount = max(maxSeqCount, seq[1], (countsSeq[i-1][1]+1) if i > 0 and charCount[countsSeq[i-1][0]] > countsSeq[i-1][1] else 0, (countsSeq[i+1][1]+1) if i < len(countsSeq)-1 and charCount[countsSeq[i+1][0]] > countsSeq[i+1][1] else 0, (countsSeq[i+1][1] + countsSeq[i-1][1] + int(charCount[countsSeq[i+1][0]] > countsSeq[i+1][1] + countsSeq[i-1][1])) if seq[1] == 1 and i > 0 and i < len(countsSeq)-1 and countsSeq[i-1][0] == countsSeq[i+1][0] else 0)
            # print(f'max at {i} - {maxSeqCount}')
            # maxSeqCount = max(maxSeqCount, seq[1], (countsSeq[i-1][1]+1) if i > 0 and charCount[countsSeq[i-1][0]] > countsSeq[i-1][1] else 0, (countsSeq[i+1][1]+1) if i < len(countsSeq)-1 and charCount[countsSeq[i+1][0]] > countsSeq[i+1][1] else 0, countsSeq[i+1][1] + countsSeq[i-1][1] + 1 if seq[1] == 1 and i > 0 and i < len(countsSeq)-1 and countsSeq[i-1][0] == countsSeq[i+1][0] and charCount[seq[0]] > seq[1] else 0)
            # maxSeqCount = max(maxSeqCount, seq[1], (countsSeq[i-1][1]+1) if i > 0 and charCount[countsSeq[i-1][0]] > countsSeq[i-1][1] else 0, (countsSeq[i+1][1]+1) if i < len(countsSeq)-1 and charCount[countsSeq[i+1][0]] > countsSeq[i+1][1] else 0)
        return maxSeqCount
                