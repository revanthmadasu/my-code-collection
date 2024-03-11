import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        while n != 0:
            n -= (2 ** math.floor(math.log(n, 2)))
            oneCount += 1
        return oneCount