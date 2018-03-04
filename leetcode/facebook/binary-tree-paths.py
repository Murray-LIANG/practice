"""
https://leetcode.com/problems/binary-tree-paths
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res

        def dfs(node, current_path):
            tmp_path = current_path + [node.val]
            if not node.left and not node.right:
                res.append('->'.join(tmp_path))
            if node.left:
                dfs(node.left, res, tmp_path)
            if node.right:
                dfs(node.right, res, tmp_path)

        dfs(root, [])
        return res

    def binaryTreePaths_2(self, root):
        res = []
        if not root:
            return res

        stack = [(root, [])]
        while stack:
            node, current_path = stack.pop()
            tmp_path = current_path + [str(node.val)]
            if not node.left and not node.right:
                res.append('->'.join(tmp_path))
            if node.right:
                stack.append((node.right, tmp_path))
            if node.left:
                stack.append((node.left, tmp_path))
        return res

