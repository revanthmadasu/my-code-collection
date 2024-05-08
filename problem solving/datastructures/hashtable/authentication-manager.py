'''
    Problem: https://leetcode.com/problems/design-authentication-manager/
    Concepts: HashTable, Design
    performance: 5.03% runtime, 80.31% memory
    #todo: improve runtime
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
        # print(f'count - cur: {currentTime}')
        x = {token: self.tokens[token] for token in self.tokens}
        # print(f'{x}')
        return len([token for token in self.tokens if self.tokens[token] > currentTime])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)