class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        i = 0
        while i < len(nums):
            num_i = nums[i]
            target = 0 - num_i
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    num_j = nums[j]
                    num_k = nums[k]
                    print(i, j, k)
                    result.append([num_i, num_j, num_k])
                    while j < k and nums[j] == num_j:
                        j += 1
                    while j < k and nums[k] == num_k:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
            while i < len(nums) and nums[i] == num_i:
                i += 1

        return result

if __name__ == '__main__':
    datas = [
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
    ]

    for nums, expected in datas:
        result = Solution().threeSum(nums)
        print('nums: {}. Three sum: {}. Expected: {}'.format(
            nums, result, sorted(expected) == sorted(result)))
