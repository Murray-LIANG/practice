//
// Created by liangr on 8/27/17.
//

// https://leetcode.com/problems/minimum-height-trees

#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>> &edges) {
        if (edges.size() == 0) {
            return vector<int>(1, 0);
        }
        vector<unordered_set<int>> neighbors(n);

        for (auto edge : edges) {
            neighbors[edge.first].insert(edge.second);
            neighbors[edge.second].insert(edge.first);
        }

        vector<int> leaves;
        for (int i=0; i<n; i++) {
            if (neighbors[i].size() == 1) {
                leaves.push_back(i);
            }
        }

        while (n>2) {
            n -= leaves.size();

            vector<int> newLeaves;
            for (auto leaf:leaves) {
                for (auto nb:neighbors[leaf]) {
                    neighbors[nb].erase(leaf);
                    if (neighbors[nb].size()==1) {
                        newLeaves.push_back(nb);
                    }
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
};

