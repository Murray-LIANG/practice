class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        if sz == 0 or sz == 1:
            return

        for i in range(sz-1, -1, -1):
            if i > 0 and nums[i-1] < nums[i]:
                break

        nums[i:] = nums[i:][::-1]

        for j in range(i, sz):
            if nums[i-1] < nums[j]:
                break
        nums[i-1], nums[j] = nums[j], nums[i-1]
        return

if __name__ == '__main__':
    cases = [
        [2,1,5,3,4],
        [2,1,3,4,5,6],
        [2,1,6,5,4,2],
        [2,5,6,5,4,2],
        [2,5,6,4,3,2],
        [3,2,1]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        (solution.nextPermutation(case))
        print(case)

