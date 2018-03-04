class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        # Solution with sort which modifies the original nums.
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                i += 1
            else:
                return i
        return -1
        """

        if not nums or len(nums) == 1:
            return -1

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]

        return fast

if __name__ == '__main__':
    datas = [
        ([1, 2, 3, 4, 1], 1),
        ([2, 2, 3, 4, 1], 2),
        ([2, 2, 3, 4, 2], 2),
        ([2, 1, 3, 4, 3], 3),
        ([1, 1], 1),
    ]

    for nums, expected in datas:

        result = Solution().findDuplicate(nums)
        print('nums: {}. Result: {}. Expected: {}'.format(
            nums, result, expected == result))
