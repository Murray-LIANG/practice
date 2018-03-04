class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sz = len(nums) - 1
        
        l = 0
        r = sz
        resultL = -1
        resultR = -1
        while l <= r:
            c = (l+r) / 2
            
            if nums[c] < target:
                l = c + 1
            elif nums[c] > target:
                r = c - 1
            else:
                i = l
                j = c - 1
                while i < j:
                    m = (i+j) / 2
                    if nums[m] == target:
                        j = m - 1
                    else:
                        i = m + 1
                if nums[i] == target:
                    resultL = i
                else:
                    resultL = i + 1
                
                i = c + 1
                j = r
                while i < j:
                    m = (i+j) / 2
                    if nums[m] == target:
                        i = m + 1
                    else:
                        j = m - 1
                print(i,j)
                if nums[j] == target:
                    resultR = j
                else:
                    resultR = j - 1
                break
                    
        return [resultL, resultR]

if __name__ == '__main__':
    cases = [
        ([2,3,3,4,4,6], 2),
        ([2,3,3,4,4,6], 3),
        ([2,3,3,4,4,6], 4),
        ([2,3,3,4,4,6], 6),
        ([2,3,3,4,4,6], 5),
        ([2,3,3,3,4,4,6], 3),
        ([2,3,3,3,4,4,6], 4),
        ([2,3,3,3,4,4,6], 5),
        ([1,2,2,3,3,3,4,5,5,7], 7),
    ]

    solution = Solution()
    for case in cases:
        print(case[0], case[1])
        print(solution.searchRange(case[0], case[1]))
