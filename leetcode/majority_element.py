class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sz = len(nums)
        if sz == 0:
            return None

        cache = None
        counter = 0
        for i in range(0, sz):
            if cache is None:
                cache = nums[i]
                counter = 1
            elif nums[i] == cache:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    cache = None
            print(i, cache, counter)
        
        return cache

if __name__ == '__main__':
    cases = [
        [1,1,2,2,2],
        [1,1,2,2,2,2],
        [1,2,1,2,1,2,2],
        [1,2,2,1,2,1,2],
        [2,1,2,1,2,1,2],
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.majorityElement(case))

