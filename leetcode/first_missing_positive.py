class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sz = len(nums)
        if sz == 0:
            return 0

        i = 0
        while i < sz:
            tmp = nums[i]-1
            if nums[i] == i + 1 \
                    or nums[i] <= 0 \
                    or nums[i] > sz \
                    or nums[i] == nums[tmp]:
                i += 1
                continue
            
            nums[i], nums[tmp] = nums[tmp], nums[i]
        
        print(nums)
        for i in range(0, sz):
            if nums[i] != i+1:
                return i+1

        return sz+1

if __name__ == '__main__':
    cases = [
        [5,3,2,4,-1,1],
        [4,3,2,1],
        [0,3,2,1],
        [3,4,1,7,6],
        [3,4,-1,1],
        [1,1],
    ]

    for case in cases:
        print('case:', case)
        print(Solution().firstMissingPositive(case))



