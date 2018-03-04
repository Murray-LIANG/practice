class Solution(object):
    def minNMaxOf3 (self, first, second, third):
        tmp = [first, second, third]
        tmp.sort()
        return [tmp[0], tmp[-1]]

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sz = len(nums)

        maxProduct = nums[0]
        tmpMin = nums[0]
        tmpMax = nums[0]
        for num in nums:
            tmpMin, tmpMax = self.minNMaxOf3(num, tmpMin*num, tmpMax*num)
            if tmpMax > maxProduct:
                maxProduct = tmpMax
        return maxProduct

if __name__ == '__main__':
    cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1,2,-1,-2,2,1,-2,1,4,-5,4],
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.maxProduct(case))

