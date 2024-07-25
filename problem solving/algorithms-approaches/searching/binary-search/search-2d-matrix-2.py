'''
    problem: https://leetcode.com/problems/search-a-2d-matrix-ii
    concepts: binary search
    performance: 50.42% runtime, 7.74% memory
'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, searchNum):
            start = 0
            end = len(nums)-1
            # print(f'searching for {searchNum} in {nums}')
            while start < end and end < len(nums):
                # print(f'start is {start}, end is {end}')
                mid = (start + end) //2
                if nums[mid] > searchNum:
                    end = mid
                elif nums[mid] == searchNum:
                    return mid
                elif nums[mid] < searchNum:
                    start = mid + 1
            # print(f'out of loop. start is {start}, end is {end}')
            if nums[start] == searchNum:
                return start
            if nums[start] > searchNum:
                return start
            else:
                return start+1
        m, n = len(matrix), len(matrix[0])

        lastRow = [matrix[m-1][i]for i in range(n)]
        firstRow = [matrix[0][i]for i in range(n)]
        left = binarySearch(lastRow, target)
        right = binarySearch(firstRow, target)
        # print(f'boundaries; left: {left}, right: {right}')
        if left >= n:
            return False
        if right >= n:
            right = n-1
        rightCol = [matrix[i][right]for i in range(m)]
        leftCol = [matrix[i][left]for i in range(m)]
        top = binarySearch(rightCol, target)
        bottom = binarySearch(leftCol, target)
        # print(f'boundaries; left: {left}, right: {right}, top: {top}, bottom: {bottom}')
        if top >= m:
            return False
        if bottom >= m:
            bottom = m-1
        for col in range(left, right+1):
            nums = [matrix[i][col]for i in range(top, bottom+1)]
            # print(f'searching {nums}')
            searchIndex = binarySearch(nums, target)
            if searchIndex < len(nums) and nums[searchIndex] == target:
                return True
        return False
            