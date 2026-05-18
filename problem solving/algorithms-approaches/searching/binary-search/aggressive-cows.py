'''
    problem: https://www.geeksforgeeks.org/problems/aggressive-cows
    concepts: binary search
    performance: 35.73% runtime, 91.16% memory
'''
class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()
        def isPossible(minDistance):
            count = 1
            prevPos = stalls[0]
            for stall in stalls[1:]:
                if stall - prevPos >= minDistance:
                    prevPos = stall
                    count += 1
                    if count == k:
                        return True
            return count >= k
        k_min = 1
        k_max = stalls[len(stalls)-1]
        
        l, r = k_min, k_max
        # print(f'kmin: {k_min}, kmax: {k_max}')
        maxPossible = 1
        while l <= r:
            mid = (l+r)//2
            # print(f'testing for mid {mid}')
            if isPossible(mid):
                if l == r:
                    return mid
                # print(f'possible')
                maxPossible = max(maxPossible, mid)
                l = mid+1
            else:
                # print(f'not possible')
                r = mid-1
        return maxPossible