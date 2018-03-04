"""
https://leetcode.com/problems/3sum
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []
        n, i = len(nums), 0
        while i < n:
            num_i = nums[i]
            target = 0 - num_i
            j, k = i+1, n-1
            while j < k:
                num_j, num_k = nums[j], nums[k]
                if num_j + num_k == target:
                    res.append((num_i, num_j, num_k))
                    while j < k and nums[j] == num_j:
                        j += 1
                    while j < k and nums[k] == num_k:
                        k -= 1
                elif num_j + num_k < target:
                    j += 1
                else:
                    k -= 1
            while i < n and nums[i] == num_i:
                i += 1
        return res
