#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> tmp_hash;
            vector<int> result;
            for (int i = 0; i < nums.size(); i++) {
                int toFind = target - nums[i];

                if (tmp_hash.find(toFind) != tmp_hash.end()) {
                    result.push_back(tmp_hash[toFind]);
                    result.push_back(i);
                    return result;
                }
                else {
                    tmp_hash[nums[i]] = i;
                }
            }
            return result;
        }
};

int main() {
    Solution s;
    vector<int> nums = {2, 4, 8, 11};
    vector<int> result = s.twoSum(nums, 10);
    for (int i: result)
        std::cout << i << std::endl;
}
