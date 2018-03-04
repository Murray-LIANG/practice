//
// Created by liangr on 8/27/17.
//

// https://leetcode.com/problems/longest-palindromic-substring

#include <string>
#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    string longestPalindrome_DP(string s) {
        /*
         * DP solution:
         * Set dp[i][j] represent whether s[i..j] is a palindrome substring or not.
         * Then whether s[i..j] is a palindrome string or not, depends on s[i] == s[j] && dp[i+1][j-1].
         *
         * For i = 0 -> n-1, j = i -> 0, dp[i][j] = s[i]==s[j] && dp[i+1][j-1]
         */

        int n = s.size();
        string res = "";
        vector<vector<bool>> dp = vector<vector<bool>>();
        for (int i = 0; i < n; i++) {
            dp.push_back(vector<bool>(n, false));
        }

        for (int j = 0; j < n; j++) {
            for (int i = j; i >= 0; i--) {
                bool tmp = s[i] == s[j] && (j - i < 3 || dp[i + 1][j - 1]);
                //dp[i][j] = s[i] == s[j] && (j - i < 3 || dp[i + 1][j - 1]);
                for (auto t:dp[i]) {

                }
                std::cout << dp[i][j] << std::endl;
                dp[i][j] = tmp;

                if (dp[i][j] && j - i + 1 > res.size()) {
                    res = s.substr(i, j - i + 1);
                }
            }
        }
        return res;
    }

    string longestPalindrome(string s) {
        /*
         * Take I as the mid, and extend the boundary one char by one char.
         * Note that need to consider two cases here:
         * One is I as the mid.
         * The other is I and I+1 as the mid.
         */

        for (int i = 0; i<s.size(); i++) {
            extendPalindrome(s, i, i);
            extendPalindrome(s, i, i+1);
        }

        return s.substr(resLeft, maxSize);
    }

private:
    int resLeft;
    int maxSize;
    void extendPalindrome(string s, int left, int right) {
        for (;left >=0 && right< s.size() && s[left] == s[right]; left--, right++) {
        }

        if (right - left -1 > maxSize) {
            maxSize = right - left -1;
            resLeft = left+1;
        }

    }
};
