'''
    problem: https://leetcode.com/problems/cherry-pickup/
    concepts: DP, Matrix
    #todo: 22/54 test cases passed. complete it
'''
'''
[ 1, 1,-1]
[ 1,-1, 1]
[-1, 1, 1]

[1,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,1],
[1,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,1,1]

[ 1, 1, 0]
[ 1, 1, 1]
[ 0, 1, 1]

[
    [ 0, 1, 1, 0, 0],
    [ 1, 1, 1, 1, 0],
    [-1, 1, 1, 1,-1],
    [ 0, 1, 1, 1, 0],
    [ 1, 0,-1, 0, 0]]
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = []
        n = len(grid)
        for i in range(n):
            dp.append([])
            for j in range(n):
                dp[i].append(set())
        def dpCall(n, grid, dp, _set=False):
            for r in range(n):
                for c in range(n):
                    if grid[r][c] != -1:
                        upCell = False
                        leftCell = False
                        maxCell = set()
                        if c-1 >= 0 and grid[r][c-1] != -1:
                            maxCell = dp[r][c-1] if len(dp[r][c-1]) > len(maxCell) else maxCell
                            leftCell = True
                        if r-1 >= 0 and grid[r-1][c] != -1:
                            maxCell = dp[r-1][c]
                            upCell = True
                        if leftCell or upCell or (r==0 and c == 0):
                            dp[r][c] = dp[r][c].union(maxCell)
                            if grid[r][c] == 1 and _set:
                                dp[r][c].add((r,c))
                        else:
                            grid[r][c] = -1
        dpCall(n, grid, dp, _set=True)
        pickedCherries = dp[n-1][n-1]
        if grid[n-1][n-1] == -1:
            return 0
        pickedCherriesHomeToEnd = len(pickedCherries)
        print(f'home to end: {pickedCherries}')
        for r in range(n):
            for c in range(n):
                dp[r][c] = dp[r][c].difference(dp[n-1][n-1])
        # print(dp)
        dp.reverse()
        grid.reverse()
        for r in range(n):
            dp[r].reverse()
            grid[r].reverse()
        print(dp)
        dpCall(n, grid, dp)
        pickedCherriesEndToHome = len(dp[n-1][n-1])
        print(f'end to home: {dp[n-1][n-1]}')
        return pickedCherriesHomeToEnd + pickedCherriesEndToHome
        