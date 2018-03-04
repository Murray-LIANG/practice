# https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1
        while i >= 0:
            while i >= 0 and nums[i] != 0:
                i -= 1
            if i < 0:
                break
            j, k = i, i + 1
            while k < len(nums) and nums[k] != 0:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
                k += 1
            i -= 1

    def moveZeroes_1(self, nums):
        # This solution is copied from discuss.
        next_slot = 0
        for num in nums:
            if num != 0:
                nums[next_slot] = num
                next_slot += 1

        while next_slot < len(nums):
            nums[next_slot] = 0
            next_slot += 1


nums = [0, 1, 0, 12, 3]
Solution().moveZeroes_1(nums)
print(nums)

nums = [1, 0, 12, 3]
Solution().moveZeroes_1(nums)
print(nums)

nums = [0]
Solution().moveZeroes_1(nums)
print(nums)
