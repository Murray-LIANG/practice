class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        for n in nums:
            if i < 2:
                nums[i] = n
                i += 1
            elif n > nums[i - 2]:
                nums[i] = n
                i += 1

        return i

if __name__ == '__main__':
    datas = [
        ([1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5], 9),
        ([1, 1], 2),
        ([1, 1, 2], 3),
    ]

    for nums, expected in datas:
        result = Solution().removeDuplicates(nums)
        print('nums: {}. Result: {}. Expected: {}'.format(
            nums, result, expected == result))
