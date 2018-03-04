class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sz = len(nums)
        if sz == 0:
            return None

        left = 0
        right = sz -1
        while left <= right:
            if left == right:
                return left
            mid = (left+right) / 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1


if __name__ == '__main__':
    cases = [1,2,3,4,5,6,7]

    for case in cases:
        print(case)
        print(Solution().generateMatrix(case))

