class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                j += 1
                nums[j] = nums[i]

        return j + 1

if __name__ == '__main__':
    datas = [
        ([1, 1, 2, 2, 3, 4], 4),
    ]

    for nums, expected in datas:
        result = Solution().removeDuplicates(nums)
        print('nums: {}. Result: {}. Expected: {}'.format(
            nums, result, expected == result))
