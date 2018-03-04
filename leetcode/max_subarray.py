class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.maxSum(nums, 0, len(nums)-1)

if __name__ == '__main__':
    cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.maxSubArray(case))

