# https://leetcode.com/problems/unique-paths/description/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        dp(i, j) = dp(i-1, j) + dp(i, j-1)
        """
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[n-1]

