"""
https://leetcode.com/problems/regular-expression-matching/

Let dp[i][j] denote whether s[:i] matches p[:j],
while 1 <= i <= len(s), 1 <= j <= len(p)

From the view of pattern, we derive dp[i+1][j+1] from:
1. if p[j] == '.' or p[j] == s[i], then dp[i+1][j+1] = dp[i][j]
2, if p[j] == '*', then
    2.1 if p[j-1] != s[i], then dp[i+1][j+1] = dp[i+1][j-1]
    2.2 if p[j-1] == '.' or p[j-1] == s[i], then dp[i+1][j+1] = any(
        dp[i+1][j-1], dp[i+1][j], dp[i][j+1])

dp[0][0] = True
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(n):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]

        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] == '.' or p[j-1] == s[i]:
                        dp[i+1][j+1] = any((dp[i+1][j-1], dp[i+1][j],
                                            dp[i][j+1]))
                    elif p[j-1] != s[i]:
                        dp[i+1][j+1] = dp[i+1][j-1]
        return dp[m][n]
