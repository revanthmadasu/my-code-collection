'''
    problem: https://leetcode.com/problems/odd-even-jump/
    concepts: Dynamic Programming, Monotonic Stack
    performance: 59.04% runtime, 93.17% memory
'''
'''
[ 0, 1,2, 3, 4, 5, 6, 7]
[10,13,5,12,14,14,13,15]
[ 3, 6,3, 6, 5, 7, 7, *] - odd
[ 2, 6,N, N, 5, 6, N, *] - even

[-1, 2,-1,-1,3, 3, 1, 3] - dp, ans 6
===============
[ 0, 1, 2, 3, 4]

[ 2, 3, 1, 1, 4]

[ 1, 4, 3, 4, *] - odd
[ 2, 2, 3, N, *] - even

[-1, 1, 2, 1, 3] - dp, ans 3
'''
from typing import List
'''

[ 2, 0, 3, 1, 6, 4, 5, 7] - sorted indices
[ 0, 1,2, 3, 4, 5, 6, 7]
[10,13,5,12,14,14,13,15]
[ 3, 6,3, 6, 5, 7, 7, *] - odd
[ 2, 6,N, N, 5, 6, N, *] - even

[-1, 2,-1,-1,3, 3, 1, 3] - dp, ans 6
===============
[ 0, 1, 2, 3, 4]

[ 2, 3, 1, 1, 4]

[ 1, 4, 3, 4, *] - odd
[ 2, 2, 3, N, *] - even

[-1, 1, 2, 1, 3] - dp, ans 3
'''
# from sortedcontainer import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        #stack contains indices
        sorted_indices = sorted(range(len(arr)), key=lambda i: arr[i])

        odd_jumps = [None] * len(arr)
        even_jumps = [None] * len(arr)
        print(f'sorted indices: {sorted_indices}')
        for ii, i in enumerate(sorted_indices):
            ji = ii+1
            while ji < len(sorted_indices) and sorted_indices[ji] < i:
                ji += 1
            if ji < len(sorted_indices):
                odd_jumps[i] = sorted_indices[ji]
        # sorted_indices = sorted(range(len(arr)), key=lambda i: -arr[i])
        # print(f'sorted indices for even {sorted_indices}')
        for ii, i in enumerate(sorted_indices):
            ji = ii-1
            if ii+1 < len(sorted_indices) and arr[i] == arr[sorted_indices[ii+1]]:
                even_jumps[i] = sorted_indices[ii+1]
                continue
            while ji >= 0 and sorted_indices[ji] < i:
                ji -= 1
            if ji >= 0:
                while ji-1 >= 0 and arr[sorted_indices[ji-1]] == arr[sorted_indices[ji]] and sorted_indices[ji-1] > i:
                    ji -= 1
                even_jumps[i] = sorted_indices[ji]
        # jump calculation using monotonic stacks - n^2 complexity worst case
        # for i in range(len(arr)-1, -1, -1):
        #     num = arr[i]
        #     found = False
        #     while len(monotonic_stack) and arr[monotonic_stack[-1]] < num:
        #         buffer_stack.append(monotonic_stack.pop())
        #     if len(monotonic_stack):
        #         odd_jumps.append(monotonic_stack[-1])
        #     else:
        #         odd_jumps.append(None)
        #     monotonic_stack.append(i)
        #     while len(buffer_stack):
        #         monotonic_stack.append(buffer_stack.pop())
        # odd_jumps.reverse()
        # buffer_stack = []
        # monotonic_stack = []
        # for i in range(len(arr)-1, -1, -1):
        #     num = arr[i]
        #     found = False
        #     while len(monotonic_stack) and arr[monotonic_stack[-1]] > num:
        #         buffer_stack.append(monotonic_stack.pop())
        #     if len(monotonic_stack):
        #         even_jumps.append(monotonic_stack[-1])
        #     else:
        #         even_jumps.append(None)
        #     monotonic_stack.append(i)
        #     while len(buffer_stack):
        #         monotonic_stack.append(buffer_stack.pop())
        # even_jumps.reverse()
        # print(f'odd jumps {odd_jumps}')
        # print(f'even jumps {even_jumps}')
        dp = [0] * len(arr)
        dp[-1] = 3
        for i in range(len(arr)-2, -1, -1):
            # oddJumpIndex = odd_jumps[i]
            # evenJumpIndex = even_jumps[i]
            if odd_jumps[i]:
                nextJumpType = dp[odd_jumps[i]]
                if nextJumpType in [3, 2]:
                    dp[i] += 1
            if even_jumps[i]:
                nextJumpType = dp[even_jumps[i]]
                if nextJumpType in [3, 1]:
                    dp[i] += 2
        return len([jumpType for jumpType in dp if jumpType in [1,3]])