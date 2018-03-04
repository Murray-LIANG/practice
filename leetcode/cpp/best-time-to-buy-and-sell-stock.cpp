//
// Created by liangr on 8/30/17.
//

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {

        int maxProfit = 0;
        int minPrice = INT_MAX;

        for (auto price:prices) {
            if (price < minPrice) {
                minPrice = price;
            }

            if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }
};

