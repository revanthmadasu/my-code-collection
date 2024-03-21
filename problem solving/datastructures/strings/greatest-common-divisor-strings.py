'''
    problem: https://leetcode.com/problems/greatest-common-divisor-of-strings
    concepts: string, math
    performance: 42.30% runtime, 26.27% memory
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        
        biggerStr, smallerStr = (str1, str2) if len(str1) > len(str2) else (str2, str1)
        remainder = len(biggerStr)%len(smallerStr)
        if not remainder:
            quotient = len(biggerStr)//len(smallerStr)
            if smallerStr * quotient == biggerStr:
                return smallerStr
            else:
                return ""
        while True:
            quotient = len(biggerStr)//len(smallerStr)
            if smallerStr * quotient + (smallerStr[:remainder]) == biggerStr:
                biggerStr = smallerStr
                smallerStr = smallerStr[:remainder]
                remainder = len(biggerStr)%len(smallerStr)
                if not remainder:
                    quotient = len(biggerStr)//len(smallerStr)
                    if smallerStr * quotient == biggerStr:
                        return smallerStr
                    else:
                        return ""
            else:
                return ""
        return ""

