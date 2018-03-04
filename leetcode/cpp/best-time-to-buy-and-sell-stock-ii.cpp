//
// Created by liangr on 8/30/17.
//

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int res = 0;
        if (prices.size()==0) {
            return res;
        }
        int lastBuyPrice = prices[0];

        prices.push_back(0);

        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < prices[i-1]) {
                res += prices[i-1] - lastBuyPrice;
                lastBuyPrice = prices[i];
            }
        }
        return res;

    }
};
