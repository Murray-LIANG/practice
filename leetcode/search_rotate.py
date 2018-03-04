class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        size = len(nums)
        
        l = 0
        r = size - 1
        
        while l <= r:
            c = (l + r) / 2
            
            if nums[c] == target:
                return c
            elif nums[c] < nums[r]:
                if nums[c] < target and target <= nums[r]:
                    l = c + 1
                else:
                    r = c - 1
            else:
                if nums[l] <= target and target < nums[c]:
                    r = c - 1
                else:
                    l = c + 1
        
        return -1

if __name__ == '__main__':
    cases = [
        ([6,7,0,1,2,4,5], 6),
        ([6,7,0,1,2,4,5], 7),
        ([6,7,0,1,2,4,5], 0),
        ([6,7,0,1,2,4,5], 1),
        ([6,7,0,1,2,4,5], 2),
        ([6,7,0,1,2,4,5], 4),
        ([6,7,0,1,2,4,5], 5),
        ([6,7,0,1,2,4,5], 3),
        ([6,7,0,2,4,5], 6),
        ([6,7,0,2,4,5], 7),
        ([6,7,0,2,4,5], 0),
        ([6,7,0,2,4,5], 2),
        ([6,7,0,2,4,5], 4),
        ([6,7,0,2,4,5], 5),
        ([6,7,0,2,4,5], 1),
        ([6,7,0,2,4,5], 3)
    ]

    solution = Solution()
    for case in cases:
        print(case[0], case[1])
        print(solution.search(case[0], case[1]))
