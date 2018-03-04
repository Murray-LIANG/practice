# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, num):

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return num * 10 + root.val

        left = (0 if root.left is None
                else self.helper(root.left, num * 10 + root.val))
        right = (0 if root.right is None
                 else self.helper(root.right, num * 10 + root.val))

        return left + right

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n2.left = n3
    n2.right = n4
    n1.right = n5
    result = Solution().sumNumbers(n1)
    print('Result: {}. Expected: {}.'.format(result, result==262))


