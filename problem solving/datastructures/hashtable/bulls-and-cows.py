'''
    problem: https://leetcode.com/problems/bulls-and-cows
    concepts: Hashtable
    performance: 89.18% runtime, 16.51% memory
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCharCount = dict()
        guessCharCount = dict()
        bullCount = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bullCount += 1
            else:
                if guess[i] not in guessCharCount:
                    guessCharCount[guess[i]] = 0
                guessCharCount[guess[i]] += 1

                if secret[i] not in secretCharCount:
                    secretCharCount[secret[i]] = 0
                secretCharCount[secret[i]] += 1
        cowCount = 0
        for ch in guessCharCount:
            if ch in secretCharCount:
                cowCount += min(secretCharCount[ch], guessCharCount[ch])
        return f'{bullCount}A{cowCount}B'
            