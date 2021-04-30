#给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#leetcode 64 最小路径合
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,colums = len(grid),len(grid[0])
        dp = [[0]*colums for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1,colums):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1,rows):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for i in range(1,rows):
            for j in range(1,colums):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[rows-1][colums-1]