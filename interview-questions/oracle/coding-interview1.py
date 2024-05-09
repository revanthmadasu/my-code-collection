
def convertToNum(romanStr):
    valuesMap = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = valuesMap[romanStr[0]]
    for i in range(1, len(romanStr)):
        sym = romanStr[i]
        prevSym = romanStr[i-1]
        if valuesMap[sym] > valuesMap[prevSym]:
            res -= (2 * valuesMap[prevSym])
        res += valuesMap[sym]
    return res
print(convertToNum('CXLVII'))
print(convertToNum('MCMXCIV'))
'''
MCMXCIV
98 - 
'''