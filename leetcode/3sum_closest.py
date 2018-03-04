class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        result = 0
        nums.sort()

        closest = 2 ** 32

        i = 0
        while i < len(nums):
            tmp_target = target - nums[i]

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == tmp_target:
                    return 0
                elif nums[j] + nums[k] < tmp_target:
                    if tmp_target - nums[j] - nums[k] < closest:
                        closest = tmp_target - nums[j] - nums[k]
                        result = target - closest
                    j += 1
                else:
                    if nums[j] + nums[k] - tmp_target < closest:
                        closest = nums[j] + nums[k] - tmp_target
                        result = target + closest
                    k -= 1

            i += 1

        return result

if __name__ == '__main__':
    datas = [
        ([-1, 2, 1, -4], 1, 2),
    ]

    for nums, target, expected in datas:
        result = Solution().threeSumClosest(nums, target)
        print('nums: {}. target: {}. Closest: {}. Expected: {}'.format(
            nums, target, result, expected == result))
