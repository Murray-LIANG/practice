//
// Created by liangr on 8/27/17.
//

// https://leetcode.com/problems/add-strings/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addStrings(string num1, string num2) {

        string res = "";
        int i = num1.size() - 1;
        int j = num2.size() - 1;

        int carry = 0;

        while (i >= 0 || j >= 0 || carry) {
            long sum = 0;
            if (i>=0) {
                sum+= num1[i] - '0';
                i--;
            }
            if (j>=0) {
                sum += num2[j] - '0';
                j--;
            }

            sum += carry;
            carry = sum/10;
            sum %= 10;
            res = res + to_string(sum);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};