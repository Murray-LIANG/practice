//
// Created by liangr on 8/28/17.
//

// https://leetcode.com/problems/unique-paths-ii

#include <vector>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid) {
        int m = obstacleGrid.size();
        if (m == 0) {
            return 0;
        }
        int n = obstacleGrid[0].size();

        vector<int> dp(n, 0);
        if (obstacleGrid[0][0] != 1) {
            dp[0] = 1;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }
};

