class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sz = len(nums)
        if sz == 0:
            return None

        cache1 = None
        counter1 = 0
        cache2 = None
        counter2 = 0
        for i in range(0, sz):
            if cache1 is None:
                cache1 = nums[i]
                counter1 = 1
            elif nums[i] == cache1:
                counter1 += 1
            elif cache2 is None:
                cache2 = nums[i]
                counter2 = 1
            elif nums[i] == cache2:
                counter2 += 1
            else:
                counter1 -= 1
                if counter1 == 0:
                    cache1 = None
                counter2 -= 1
                if counter2 == 0:
                    cache2 = None
            print(i, cache1, counter1, cache2, counter2)

        if cache1 is None and cache2 is None:
            return None
        
        check1 = 0
        check2 = 0
        for num in nums:
            if cache1 is not None and num == cache1:
                check1 += 1
            elif cache2 is not None and num == cache2:
                check2 += 1

        result = []
        if check1 > sz / 3:
            result.append(cache1)
        if check2 > sz / 3:
            result.append(cache2)

        return result

if __name__ == '__main__':
    cases = [
        [1,2,3,1,2,3,1],
        [1,2,3,1,2,3,1,2],
        [1,2,3,1,2,3,1,2,3],
        [1,1,1,1,2,3,1],
        [1,1,1,2,2,3,2],
        [1,1,1,2,2,3,3],
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.majorityElement(case))

