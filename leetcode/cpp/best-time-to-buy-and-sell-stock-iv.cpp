//
// Created by liangr on 8/30/17.
//

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(int K, vector<int> &prices) {
        // Copied from best-time-to-buy-and-sell-stock-iii

        if (prices.size() == 0) {
            return 0;
        }
        // int K = 2;

        vector<vector<int>> dp(K + 1, vector<int>(prices.size(), 0));

        for (int k = 1; k <= K; k++) {
            int maxJ = dp[k - 1][0] - prices[0];
            for (int i = 1; i < prices.size(); i++) {
                dp[k][i] = max(dp[k][i - 1], maxJ + prices[i]);
                maxJ = max(maxJ, dp[k - 1][i] - prices[i]);
            }
        }
        return dp[K][prices.size() - 1];
    }
};
