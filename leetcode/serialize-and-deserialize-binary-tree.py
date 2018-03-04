# https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = []

        def preorder(node):
            if node:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                res.append('#')

        preorder(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data_iter = iter(data.split())

        def preorder():
            current = next(data_iter)
            if current == '#':
                return None

            root = TreeNode(int(current))
            left = preorder()
            right = preorder()
            root.left, root.right = left, right
            return root

        return preorder()


# Your Codec object will be instantiated and called as such:
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left, n1.right = n2, n3
n2.left, n2.right = None, n4
n3.left, n3.right = n5, n6
n5.left, n5.right = None, n7

codec = Codec()
ser = codec.serialize(n1)
des = codec.deserialize(ser)
print('end')
