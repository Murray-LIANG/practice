
# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, sum, res, [])
        return res

    @staticmethod
    def dfs(node, remaining, res, path):
        if not node or remaining < node.val:
            return

        if remaining == node.val and not node.left and not node.right:
            res.append(path + [node.val])
            return

        Solution.dfs(node.left, remaining - node.val, res, path + [node.val])
        Solution.dfs(node.right, remaining - node.val, res, path + [node.val])


n5 = TreeNode(5)
n4 = TreeNode(4)
n8 = TreeNode(8)
n11 = TreeNode(11)
n13 = TreeNode(13)
n4_2 = TreeNode(4)
n7 = TreeNode(7)
n2 = TreeNode(2)
n5_2 = TreeNode(5)
n1 = TreeNode(1)
n5.left, n5.right = n4, n8
n4.left = n11
n8.left, n8.right = n13, n4_2
n11.left, n11.right = n7, n2
n4_2.left, n4_2.right = n5_2, n1
print(Solution().pathSum(n5, 22))
