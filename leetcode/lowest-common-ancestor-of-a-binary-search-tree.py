# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root.val
        elif p.val < root.val < q.val or q.val < root.val < p.val:
            return root.val
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)

n6.left, n6.right = n2, n8
n2.left, n2.right = n0, n4
n4.left, n4.right = n3, n5
n8.left, n8.right = n7, n9

print(Solution().lowestCommonAncestor(n6, n2, n4))
print(Solution().lowestCommonAncestor(n6, n7, n4))
print(Solution().lowestCommonAncestor(n6, n3, n5))
