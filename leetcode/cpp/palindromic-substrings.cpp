//
// Created by liangr on 8/28/17.
//

// https://leetcode.com/problems/palindromic-substrings

#include <string>

using namespace std;

class Solution {
public:
    int countSubstrings(string s) {

        count = 0;
        for (int i = 0; i < s.size(); i++) {
            extendPalindrome(s, i, i);
            extendPalindrome(s, i, i + 1);
        }
        return count;
    }

private:
    int count;

    void extendPalindrome(string s, int left, int right) {
        for (; left >= 0 && right < s.size() && s[left] == s[right]; left++, right--) {
            count++;
        }
    }
};

