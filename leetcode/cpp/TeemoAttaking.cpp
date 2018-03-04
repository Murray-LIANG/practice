//
// Created by liangr on 8/27/17.
//
//https://leetcode.com/problems/teemo-attacking/description/

#include <vector>

class TeemoAttaking {
public:
    int findPoisonedDuration(std::vector<int> &timeSeries, int duration) {
        int res = 0;
        for (int i = 1; i < timeSeries.size(); i++) {
            res += timeSeries[i] - timeSeries[i - 1] >= duration ? duration : timeSeries[i] - timeSeries[i - 1];
        }
        if (timeSeries.size() != 0) {
            res += duration;
        }
        return res;

    }
};
