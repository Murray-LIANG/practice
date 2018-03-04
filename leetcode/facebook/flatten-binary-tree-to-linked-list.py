"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def _helper(node):
            if not node.left and not node.right:
                return node

            last_left = _helper(node.left) if node.left else None
            last_right = _helper(node.right) if node.right else None

            if last_left:
                last_left.right = node.right
                node.right = node.left
                node.left = None
                return last_right if last_right else last_left
            return last_right

        if not root:
            return
        _helper(root)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left, n1.right = n2, n3
n2.left = n4
n3.right = n5
Solution().flatten(n1)
print('Done')
