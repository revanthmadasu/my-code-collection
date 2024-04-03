'''
    problem: https://leetcode.com/problems/find-in-mountain-array
    concepts: Searching, Binary Search, Recursion
    performance: 52.98 runtime, 5.68 memory
'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binarySearch(start, end):
            # print(f'searching between {start} and {end}')
            mid = (start + end) // 2
            midNum = mountain_arr.get(mid)
            # print(f'midNum is {midNum}')
            nextToMid = None
            prevToMid = None
            side = 0
            if mid > 0:
                prevToMid = mountain_arr.get(mid-1)
            if mid < mountain_arr.length()-1:
                nextToMid = mountain_arr.get(mid+1)
            if mid > 0 and midNum > prevToMid:
                side = -1
            if mid < mountain_arr.length()-1 and nextToMid < midNum:
                side += 1
            if start == mid:
                if midNum == target:
                    # print('found')
                    return mid
                if nextToMid == target:
                    return mid + 1
                return None
            # print(f'side: {side}')
            if side == 0:
                if midNum == target:
                    return mid
                else:
                    # print(f'call1')
                    firstRes = binarySearch(start, mid)
                    if firstRes != None:
                        # print(f'found at {firstRes} between {start} and {end}')
                        return firstRes
                    return binarySearch(mid, end)
            elif side == -1:
                if midNum == target:
                    return mid
                elif midNum > target:
                    # print(f'left half, mid greater - first search in left, then right')
                    firstRes = binarySearch(start, mid)
                    if firstRes != None:
                        # print(f'found at {firstRes} between {start} and {end}')
                        return firstRes
                    return binarySearch(mid, end)
                else:
                    # print(f'left half, mid lesser')
                    return binarySearch(mid, end)
            else:
                if midNum == target:
                    firstRes = binarySearch(start, mid)
                    if firstRes != None:
                        # print(f'found at {firstRes} between {start} and {end}')
                        return firstRes
                    return mid
                elif midNum > target:                    
                    firstRes = binarySearch(start, mid)
                    if firstRes != None:
                        # print(f'found at {firstRes} between {start} and {end}')
                        return firstRes
                    return binarySearch(mid, end)
                else:
                    return binarySearch(start, mid)
        res = binarySearch(0, mountain_arr.length()-1)
        return res if res != None else -1