# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and sum == root.val:
            return True

        return (self.hasPathSum(root.left, sum - root.val)
                or self.hasPathSum(root.right, sum - root.val))

if __name__ == '__main__':
    n_5 = TreeNode(5)
    n_4 = TreeNode(4)
    n_8 = TreeNode(8)
    n_11 = TreeNode(11)
    n_13 = TreeNode(13)
    n_4_2 = TreeNode(4)
    n_7 = TreeNode(7)
    n_2 = TreeNode(2)
    n_1 = TreeNode(1)

    n_5.left = n_4
    n_5.right = n_8
    n_4.left = n_11
    n_8.left = n_13
    n_8.right = n_4_2
    n_11.left = n_7
    n_11.right = n_2
    n_4_2.right = n_1

    print(Solution().hasPathSum(n_5, 22))
