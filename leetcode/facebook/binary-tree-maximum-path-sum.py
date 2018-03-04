"""
https://leetcode.com/problems/binary-tree-maximum-path-sum
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0 - 2 ** 31


        def _helper(node):
            if not node:
                return 0

            sum_l, sum_r = max(0, _helper(node.left)), max(0, _helper(node.right))
            sum_n = node.val + sum_l + sum_r
            if sum_n > self.res:
                self.res = sum_n
            return node.val + max(sum_l, sum_r)

        _helper(root)
        return self.res


    def maxPathSum_2(self, root):
        self.res = 0 - 2 ** 31
        self.path = None

        def _helper(node):
            if not node:
                return 0, None
            sum_l, path_l = _helper(node.left)
            if sum_l <= 0:
                sum_l = 0
                path_l = None
            sum_r, path_r = _helper(node.right)
            if sum_r <= 0:
                sum_r = 0
                path_r = None
            sum_n = node.val + sum_l + sum_r
            if sum_n > self.res:
                self.res = sum_n
                self.path = TreeNode(node.val)
                self.path.left, self.path.right = path_l, path_r
            path_n = TreeNode(node.val)
            if sum_l > sum_r:
                path_n.left = path_l
                return node.val + sum_l, path_n
            else:
                path_n.right = path_r
                return node.val + sum_r, path_n

        _helper(root)
        return self.path

root = TreeNode(-5)
n2 = TreeNode(-2)
n3 = TreeNode(-3)
n4 = TreeNode(-2)
root.left, root.right = n2, n3
n2.left = n4
print(Solution().maxPathSum_2(root))


