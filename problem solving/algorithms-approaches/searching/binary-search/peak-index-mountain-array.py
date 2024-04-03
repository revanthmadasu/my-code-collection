'''
    problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/
    concepts: Searching, Binary Search, Recursion
    performance: 95.80 runtime, 7.91 memory
'''
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def binarySearch(start, end):
            if end-start <= 1:
                if start != 0:
                    if arr[start-1] < arr[start] and arr[start] > arr[end]:
                        return start
                if end != len(arr):
                    if arr[end+1] < arr[end] and arr[end] > arr[start]:
                        return end
                return None
            mid = (start + end) // 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] > arr[mid]:
                return binarySearch(start, mid)
            elif arr[mid+1] > arr[mid]:
                return binarySearch(mid, end)
            else:
                res1 = binarySearch(start, mid)
                if res1:
                    return res1
                return binarySearch(mid, end)
        return binarySearch(0, len(arr)-1)