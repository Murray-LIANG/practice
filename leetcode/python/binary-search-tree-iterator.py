"""
https://leetcode.com/problems/binary-search-tree-iterator

It just ask you to write an inorder sort using stack.
For each node, push it to stack for later using to visit its right child.
Push left child to stack until the left most one. Then pop the top of stack,
treat it as the root of a new tree.
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._traverse_left_most(root)

    def _traverse_left_most(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        left_most = self.stack.pop()
        self._traverse_left_most(left_most.right)
        return left_most.val


        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())