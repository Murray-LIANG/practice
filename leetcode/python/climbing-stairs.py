# https://leetcode.com/problems/climbing-stairs


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        DP solution: dp[i] = dp[i-1] + dp[i-2]
        dp[0] = 1, dp[1] = 1
        dp[2] = dp[1] + dp[0]
        dp[3] = dp[2] + dp[1]
        """

        dp = [1, 1]
        for _ in range(n-1):
            dp.append(dp[-1] + dp[-2])

        return dp[-1]


