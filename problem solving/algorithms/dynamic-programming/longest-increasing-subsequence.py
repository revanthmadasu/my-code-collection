#!/bin/python3
#https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem?h_r=internal-search
import math
import os
import random
import re
import sys

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestIncreasingSubsequence(arr):
    seqCountAry = [1 for i in arr]
    n = len(arr)
    maxCount = 0
    for i in range(n-1, -1, -1):
        maxPossibleIndex = -1
        addCount = 0
        for j in range(i+1, n):
            if arr[j] > arr[i] and seqCountAry[j] > addCount:
                addCount = seqCountAry[j]
        seqCountAry[i] += addCount
        if maxCount < seqCountAry[i]:
            maxCount = seqCountAry[i]
    return maxCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
