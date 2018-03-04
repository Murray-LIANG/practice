"""
https://leetcode.com/problems/move-zeroes
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        slot = 0
        for num in nums:
            if num != 0:
                nums[slot] = num
                slot += 1

        for i in range(slot, len(nums)):
            nums[i] = 0
