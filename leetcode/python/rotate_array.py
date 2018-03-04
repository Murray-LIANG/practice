# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    Solution().rotate(nums, 3)
    print('nums: {}. Expected: {}.'.format(nums, nums==[5,6,7,1,2,3,4]))


