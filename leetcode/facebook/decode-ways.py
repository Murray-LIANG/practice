"""
https://leetcode.com/problems/decode-ways
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        Use DP:
        dp(i) denotes that how many ways to decode string s[:i].
        dp(i) = (dp(i-1) if s[i-1] != '0' else 0) \
                + (dp(i-2) if 10 <= int(s[i-2:i]) <= 26 else 0)

        dp(0) = 1
        dp(1) = 1 if s[0] != '0' else 0
        """

        if not s:
            return 0
        n = len(s)
        dp = [1] + [0] * n
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n+1):
            dp[i] = (dp(i-1) if s[i-1] != '0' else 0) + \
                    (dp(i-2) if 10 <= int(s[i-2:i]) <= 26 else 0)
        return dp[n]
