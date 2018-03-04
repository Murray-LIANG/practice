//
// Created by liangr on 8/28/17.
//

// https://leetcode.com/problems/longest-palindromic-subsequence

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    /*
     * DP solution:
     * Use dp[i][j] to store the length of longest palindrome in s[i..j].
     * So
     * 1. if s[i] == s[j], dp[i][j] = dp[i+1][j-1] + 2
     * 2. else, dp[i][j] = max( dp[i+1][j], dp[i][j-1] )
     * We could use two ways to solve this DP. One is bottom up, the other is top down with memo.
     */
    int longestPalindromeSubseq_BottomUp(string s) {
        int n = s.size();
        vector<vector<int>> dp = vector<vector<int>>();
        for (int i = 0; i < n; i++) {
            dp.push_back(vector<int>(n, 0));
        }

        for (int j = 0; j < n; j++) {
            dp[j][j] = 1;
            for (int i = j - 1; i >= 0; i--) {
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }

    int longestPalindromeSubseq_TopDownWithMemo(string s) {
        int n = s.size();
        vector<vector<int>> memo = vector<vector<int>>();
        for (int i = 0; i < n; i++) {
            memo.push_back(vector<int>(n, -1));
        }

        return helper(s, 0, n-1, memo);
    }

    int helper(string s, int left, int right, vector<vector<int>> &memo) {
        if (memo[left][right] == -1) {
            if (left == right) {
                memo[left][right] = 1;
            } else if (left > right) {
                memo[left][right] = 0;
            } else {
                if (s[left] == s[right]) {
                    memo[left][right] = helper(s, left + 1, right - 1, memo) + 2;
                } else {
                    memo[left][right] = max(helper(s, left, right - 1, memo), helper(s, left + 1, right, memo));
                }
            }
        }
        return memo[left][right];
    }
};
