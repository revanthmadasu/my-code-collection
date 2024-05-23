#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'renameFile' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING newName
#  2. STRING oldName
#
'''
abcdadfbjbjfchnckdjkdjkd, abcd
abcdadbbccddda, abcd
  a b c d a d b b c c d d d a
a
b
c
d

  a b a b c c a b b c
a 15 7 7 2 2 2 2 0 0 0
b 8 8 5 5 2 2 2 2 1 0
c 3 3 3 3 3 2 1 1 1 1

  c c c c
c
c       0
c 4 3 2 1

'''
def renameFile(newName, oldName):
    # Write your code here
    dpMat = [[0 for _ in range(len(oldName)+1)] for __ in range(len(newName)+1)]
    for c in range(len(oldName)+1):
        dpMat[len(newName)][c] = 1
    for r in range(len(newName)-1, -1, -1):
        for c in range(len(oldName)-1, -1, -1):
            if newName[r] == oldName[c] and dpMat[r+1][c+1] != 0:
                dpMat[r][c] = dpMat[r+1][c+1] + dpMat[r][c+1]
            else:
                dpMat[r][c] = dpMat[r][c+1]
    # print(dpMat)
    return dpMat[0][0] % ((10**9)+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    newName = input()

    oldName = input()

    result = renameFile(newName, oldName)

    fptr.write(str(result) + '\n')

    fptr.close()
