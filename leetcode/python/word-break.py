# https://leetcode.com/problems/word-break

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        Use DP, let dp[i] denote the s[0..i) can be broken into words in
        wordDict or not.
        Then dp[i] = dp[j] and (s[j..i) is in wordDict) for j = from 0 to i-1.
        and i = from 1 to len(s).
        dp[0] = True.
        """

        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for j in range(0, i):
                dp[i] = dp[j] and s[j:i] in wordDict
                if dp[i]:
                    break

        return dp[len(s)]

print(Solution().wordBreak('faceb', ['face', 'book', 'b']))
