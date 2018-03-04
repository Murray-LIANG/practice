# https://leetcode.com/problems/sort-colors


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i, j = 0, n - 1
        while True:
            while i < n and nums[i] == 0:
                i += 1
            while j >= 0 and nums[j] != 0:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        j = n - 1
        while True:
            while i < n and nums[i] == 1:
                i += 1
            while j >= 0 and nums[j] != 1:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

    def sortColors_2(self, nums):
        n = len(nums)

        zero_end, two_start = 0, n - 1
        i = zero_end
        while i <= two_start:
            while nums[i] == 2 and i < two_start:
                nums[i], nums[two_start] = nums[two_start], nums[i]
                two_start -= 1
            while nums[i] == 0 and i > zero_end:
                nums[i], nums[zero_end] = nums[zero_end], nums[i]
                zero_end += 1
            i += 1


# nums = [0, 1, 2, 0, 0, 1, 1, 2, 1]
# Solution().sortColors_2(nums)
# print(nums)
#
# nums = [1, 0]
# Solution().sortColors_2(nums)
# print(nums)

nums = [1, 2, 0]
Solution().sortColors_2(nums)
print(nums)
