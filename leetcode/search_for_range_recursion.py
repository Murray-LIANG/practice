class Solution(object):
    def findStartNEnd(self, nums, target, l, r):
        if l >= r:
            if nums[l] == target:
                return [l,l]
            else:
                return [-1, -1]
        elif l < r:
            c = (l+r) / 2
            
            if nums[c] > target:
                return self.findStartNEnd(nums, target, l, c-1)
            elif nums[c] < target:
                return self.findStartNEnd(nums, target, c+1, r)
            else:
                tmpI, tmpC = self.findStartNEnd(nums, target, l, c-1)
                tmpC, tmpR = self.findStartNEnd(nums, target, c+1, r)
                if tmpI != -1 and tmpC != -1:
                    return [tmpI, tmpR]
                elif tmpI == -1 and tmpC != -1:
                    return [c, tmpR]
                elif tmpI != -1 and tmpC == -1:
                    return [tmpI, c]
                else:
                    return [c, c]
        
        return [-1,-1]
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        return self.findStartNEnd(nums, target, 0, len(nums)-1)

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
    ]

    solution = Solution()
    for case in cases:
        print(case[0], case[1])
        print(solution.searchRange(case[0], case[1]))
