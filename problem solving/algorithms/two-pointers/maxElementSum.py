'''
    problem: https://www.hackerrank.com/test/14j0osksnmj/questions/36i8p279n6k
    concepts: arrays, interval, math
    hidden test cases not passing but getting expected output according to problem
'''

# def maxElement(n, maxSum, k):
#     # Write your code here
#     if maxSum <= 1:
#         return maxSum
#     leftElements = k
#     rightElements = n - 1 - k
#     leftStop = leftElements > 0
#     rightStop = rightElements > 0
#     _sum = 0
#     stretch = 0
#     while not (leftStop and rightStop):
#         cur_iter_sum = (2*stretch + 1)
#         cur_stretch = stretch + 1
#         if cur_stretch > (leftElements+1):
#             n_terms = stretch - leftElements - 1
#             cur_iter_sum -= (n_terms * (n_terms + 1) * 0.5)
#             leftStop = True
#         if cur_stretch > (rightElements+1):
#             n_terms = cur_stretch - rightElements - 1
#             cur_iter_sum -= (n_terms * (n_terms + 1) * 0.5)
#             rightStop = True
#         if (_sum + cur_iter_sum) > maxSum:
#             break
#         _sum += cur_iter_sum
#         stretch = cur_stretch
#     highest = stretch
#     if _sum < maxSum:
#         # after filling up, the sum is still lesser and can fit more values in
#         available = maxSum - _sum
#         highest += int(available/n)
#     return highest

def maxElement(n, maxSum, k):
    # Write your code here
    if maxSum <= 1:
        return maxSum
    _sum = 0
    nums = [0]*n
    stretch = 0
    maxReached = False
    while True:
        start = max(0, k-stretch)
        end = min(n-1, k+stretch)
        if _sum + (end+1-start) > maxSum:
            maxReached = True
            break
        _sum += (end+1-start)
        for i in range(start, end+1):
            nums[i] += 1
        if maxReached:
            break
        stretch += 1
    return nums[k]

# print(maxElement(3, 7, 1))
# print(maxElement(4, 6, 2))
# print(maxElement(4, 4, 3))
# print(maxElement(1, 2, 0))
# print(maxElement(445, 488, 0))
# print(maxElement(445, 488, 0))
print(maxElement(522, 685, 395))