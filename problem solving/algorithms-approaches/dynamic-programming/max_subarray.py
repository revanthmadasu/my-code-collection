#!/bin/python3
# https://www.hackerrank.com/challenges/maxsubarray/problem
import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    maxSubSequence = float('-inf')
    maxSubArray = 0
    cur_sum = float('-inf')
    max_sum = float('-inf')
    for num in arr:
        maxSubSequence = max((maxSubSequence+num), num, maxSubSequence)
        cur_sum = num if cur_sum+num < num else cur_sum+num
        if max_sum < cur_sum:
            max_sum = cur_sum
    return (max_sum,maxSubSequence)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
