"""
https://leetcode.com/problems/inorder-successor-in-bst

Given a binary search tree and a node in it, find the in-order successor of
that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode

        Recursive solution: if the value of p is smaller than the one of root,
        then p's successor must be in the left subtree of root or the root
        itself (if the successor is not found under the left subtree).
        Otherwise, p's successor must be under the right subtree.
        """

        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root


    def inorderSuccessor_2(self, root, p):
        """
        :param root:
        :param p:
        :return:

        Iterative solution: store the info of the possible successor, that is,
        if the value of p is smaller than the one of root, then the possible
        successor is under the left subtree of root or the root. Otherwise
        under the right subtree. The possible successor changes only when
        entering the left subtree.
        """

        successor = None

        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

