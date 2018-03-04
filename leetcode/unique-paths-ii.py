# https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        dp(i,j) = dp(i-1,j) + dp(i, j-1) if grid[i][j] != 1
                  else 0
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [0, 1] + [0] * (n-1)

        for i in range(0, m):
            for j in range(1, n+1):
                dp[j] = dp[j-1] + dp[j] if obstacleGrid[i][j] == 0 else 0

        return dp[n]

