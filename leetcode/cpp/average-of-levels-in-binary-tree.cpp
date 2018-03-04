//
// Created by liangr on 8/27/17.
//
// https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

#include <vector>
#include <queue>
#include <cstddef>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    vector<double> averageOfLevels(TreeNode *root) {

        vector<double> res;
        queue<TreeNode *> q = queue<TreeNode *>();
        q.push(root);

        while (q.size() > 0) {
            double sum = 0;
            int count = 0;
            for (int i = q.size(); i > 0; i--) {
                TreeNode *front = q.front();
                sum += front->val;
                count++;
                q.pop();
                if (front->left) {
                    q.push(front->left);
                }
                if (front->right) {
                    q.push(front->right);
                }
            }
            res.push_back(sum / count);
        }
        return res;
    }
};
