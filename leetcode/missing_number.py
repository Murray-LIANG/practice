class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []
        
        nums.sort()
        
        result = []
        tmpI = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                remain = 0 - i -j
                l = j + 1
                r = len(nums) - 1
                print(remain, l, r)
                if remain > nums[r]:
                    continue
                elif remain == nums[r]:
                    result.append([i, j, c])
                    continue
    
                while l < r:
                    c = (l + r) / 2
                    if nums[c] == remain:
                        result.append([i, j, c])
                    elif nums[c] > remain:
                        r = c - 1
                    else:
                        l = c + 1
            