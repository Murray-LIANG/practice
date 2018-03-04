class Solution(object):
    def sortSection(cls, nums, i, j, i_color, j_color):
        while True:
            while i < len(nums) and nums[i] != j_color:
                i += 1
            while j >=0 and nums[j] != i_color:
                j -= 1

            if i < j:
                (nums[i], nums[j]) = (nums[j], nums[i])
            else:
                break

        return i

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k = self.sortSection(nums, 0, len(nums)-1, 0, 2)
        print(k)

        self.sortSection(nums, k, len(nums)-1, 1, 2)
        self.sortSection(nums, 0, k-1, 0, 1)


if __name__ == "__main__":

    nums = [1, 0, 0, 0, 2]
    print(nums)
    Solution().sortColors(nums)
    print(nums)
