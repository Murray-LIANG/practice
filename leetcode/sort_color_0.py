class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        for k in range(0, len(nums)):
            if k > j:
                break
            if nums[k] == 0:
                nums[i] = 0
                i += 1
            elif nums[k] == 2:
                if nums[j] == 0:
                    nums[i] = 0
                    i += 1
                nums[j] = 2
                j -= 1
        for k in range(i , j+1):
            nums[k] = 1

if __name__ == "__main__":

    nums = [0, 0, 1, 0, 2, 1, 0]
    print(nums)
    Solution().sortColors(nums)
    print(nums)
