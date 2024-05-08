'''
    Problem: https://leetcode.com/problems/design-authentication-manager/
    Concepts: HashTable, Design
    performance: 38.70% runtime, 96.86% memory
'''
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId] > currentTime:
                self.tokens[tokenId] = currentTime + self.timeToLive
            else:
                del self.tokens[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.tokens.copy():
            if self.tokens[token] > currentTime:
                count += 1
            else:
                del self.tokens[token]
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)