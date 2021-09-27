'''
    problem description
    Hacker has two strings S and T. He has to find the minimum (contiguous) substring Window of S. So that T is a subsequence of Window.
    Note: If there is no such Window in S that cover all characters in T, return the empty string.
    If there are multiple such minimum-length windows, return the one with the left-most starting index.

    platform: hackerearth - adobe coding interview
    
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

from collections import defaultdict
class X:
    def __init__(self, index, startingChar):
        self.index = index
        self.substring = startingChar
        self.lastSatisfiedIndex = 0
        self.satisfied = False
def getMinSubsequence(S,T):
    tCharsMap = defaultdict(lambda: [])
    collectingList = []
    for t_i in range(len(T)):
        char = T[t_i]
        if not tCharsMap[char]:
            tCharsMap[char] = [t_i]
        else:
            tCharsMap[char].append(t_i)
    for s_i in range(len(S)):
        char = S[s_i]
        for collectedObj in collectingList:
            if collectedObj.lastSatisfiedIndex != len(T) - 1:
                collectedObj.substring = collectedObj.substring + char
        if len(tCharsMap[char]) != 0:
            for index in tCharsMap[char]:
                if index == 0:
                    obj = X(s_i, char)
                    collectingList.append(obj)
                else:
                    for collectedObj in collectingList:
                        if collectedObj.lastSatisfiedIndex == index-1:
                            collectedObj.lastSatisfiedIndex = index
                        if collectedObj.lastSatisfiedIndex == len(T) - 1:
                            collectedObj.satisfied = True
    filteredItems = list(filter(lambda item: item.lastSatisfiedIndex == len(T) - 1,  collectingList))
    # print(len(filteredItems))
    # for item in filteredItems:
    #     print(item.substring)
    filteredItems.sort(key = lambda item: len(item.substring))
    print(filteredItems[0].substring if len(filteredItems) > 0 else '\n')


s, t = input().split(' ')
getMinSubsequence(s,t)
