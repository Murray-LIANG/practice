class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sz = len(nums)
        if sz == 0:
            return None

        left = 0
        right = sz -1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left+right) / 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[right]


if __name__ == '__main__':
    cases = [
        [1,2,3,4,5,6,7],
        [7,1,2,3,4,5,6],
        [7,1,2,3,4,5,],
        [6,7,1,2,3,4,5,],
        [6,7,1,2,3,4,],
        [5,6,7,1,2,3,4,],
        [5,6,7,1,2,3,],
        [4,5,6,7,1,2,3,],
        [4,5,6,7,1,2,],
        [3,4,5,6,7,1,2,],
        [3,4,5,6,7,1,],
        [2,3,4,5,6,7,1,],
        [2,3,4,5,6,7,],
    ]


    for case in cases:
        print(case)
        print(Solution().findMin(case))

