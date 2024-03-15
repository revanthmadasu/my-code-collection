'''
    get maximum sum of non consecutive elements in array
'''
from collections import defaultdict
def getNonConsecutiveMaxSum(arr):
    N = len(arr)
    # memoization
    sumsResult = defaultdict(lambda: None) # key is index
    numberOfTimesExecuted = [0]

    def recursiveSearch(i):
        numberOfTimesExecuted[0] = numberOfTimesExecuted[0] + 1
        print(f'number of times executed: {numberOfTimesExecuted[0]}')
        if N - i <= 2:
            sumsResult[i] = arr[i]
            return arr[i]
        # not doing memoization
        # res0 = recursiveSearch(i+2)
        # res1 = recursiveSearch(i+3) if i+3 < N else 0
        # memoization
        res0 = sumsResult[i+2] if sumsResult[i+2] != None else recursiveSearch(i+2)
        res1 = (sumsResult[i+3] if sumsResult[i+3] != None else recursiveSearch(i+3)) if i+3 < N else 0
        return arr[i] + max(res0, res1)
    if len(arr) == 1:
        return arr[0]
    res0 = recursiveSearch(0)
    res1 = recursiveSearch(1)
    return max(res0, res1)
arr = [35,26,40,60,41,50]
print(getNonConsecutiveMaxSum(arr))
