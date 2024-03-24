'''
    problem: https://leetcode.com/problems/sentence-screen-fitting
    concepts: string
    performance: 17.47% runtime, 81.73% memory
'''
from typing import List
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentenceCount = 0
        curCol = 0
        mySentence = " ".join(sentence) + " "
        print(f'{mySentence}')
        print(f'{len(mySentence)}')
        for row in range(rows):
            curCol += cols
            while curCol >= 0 and mySentence[curCol%len(mySentence)] != ' ':
                curCol -= 1
            # print(f'added till {curCol}')
            curCol += 1
            if curCol >= len(mySentence)-1:
                # print(f'prev: {sentenceCount} adding sen count: {(curCol//len(mySentence))} - {((curCol-cols)//len(mySentence))}')
                sentenceCount += (((curCol//len(mySentence)) - (max(curCol-cols, 0)//len(mySentence))))
                # print(f'update sentence count: {sentenceCount}')
            curCol = curCol % len(mySentence)
            # print(f'curCount updated to {curCol}')

        return sentenceCount

    '''
    # Brute force approach - timeout issues
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentenceCount = 0
        curWordtoAdd = 0
        def addWord(curWordtoAdd, sentenceCount):
            curWordtoAdd = (curWordtoAdd + 1)%len(sentence)
            if curWordtoAdd == 0:
                # print('adding sentence')
                sentenceCount += 1
            return curWordtoAdd, sentenceCount
        for row in range(rows):
            # print(f'start - ro {row}')
            capacity = cols
            newLine = True
            # capacity -= len(sentence[curWordtoAdd])
            # print(f'added {sentence[curWordtoAdd]}')
            # curWordtoAdd, sentenceCount = addWord(curWordtoAdd, sentenceCount)
            while capacity >= (len(sentence[curWordtoAdd]) +int(not newLine)):
                # print(f'added {sentence[curWordtoAdd]}')
                capacity -= (len(sentence[curWordtoAdd]) +int(not newLine))
                curWordtoAdd, sentenceCount = addWord(curWordtoAdd, sentenceCount)
                newLine = False
            # print(f'end - row {row}')

        return sentenceCount
    '''

sol = Solution()
print(sol.wordsTyping(["a"], 10000, 10000))