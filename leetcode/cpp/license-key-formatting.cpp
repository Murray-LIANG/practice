//
// Created by liangr on 8/28/17.
//

// https://leetcode.com/problems/license-key-formatting

#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string licenseKeyFormatting(string S, int K) {

        string res = "";
        for (auto i = S.rbegin(); i < S.rend(); i++) {
            char c = *i;
            if (c == '-') {
                continue;
            }
            if (res.size() % (K + 1) == K) {
                res += '-';
            }
            res += toupper(c);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
