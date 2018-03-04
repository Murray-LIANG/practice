class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        sz = len(nums)
        if sz == 0:
            return []
        
        nums.sort()
        result = [[]]
        activeNum = None

        for i in range(0, sz):
            if i > 0 and nums[i] == nums[i-1]:
                if activeNum is None:
                    activeNum = len(result) / 2
                result += [each+[nums[i]] for each in result[-activeNum:]]
            else:
                activeNum = None
                result += [each+[nums[i]] for each in result]

        return result

        

if __name__ == '__main__':
    cases = [
        #[3,2,1,0,4],
        [2,2,1,1,4],
        [1,2,2],
        [1,2,2,2,3],
        [1,1,2],
        [1,2,3,3,3]
    ]

    for case in cases:
        print(case)
        print(Solution().subsets(case))

