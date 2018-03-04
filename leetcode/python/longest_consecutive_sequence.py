class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        # Solution #1: search bi-direction.
        result = 0 # max count of longest

        m = {num: 1 for num in nums}

        for num in nums:
            if m[num] == 0:
                continue
            m[num] = 0
            tmp_max = 1

            target = num - 1
            while target in m:
                tmp_max += 1
                m[target] = 0
                target -= 1
            target = num + 1
            while target in m:
                tmp_max += 1
                m[target] = 0
                target += 1

            result = max(result, tmp_max)

        return result
        """

        # Solution #2: only search the nums in incremental order.
        result = 0 # max count of longest

        nums = set(nums) # O(1) to check the x in set of nums or not.

        for num in nums:
            if num - 1 not in nums:
                target = num + 1
                while target in nums:
                    target += 1

                result = max(result, target - num)

        return result




if __name__ == '__main__':
    datas = [
        ([], 0),
        ([1], 1),
        ([1,1,1,1], 1),
        ([1,2,3,4,1,1,1], 4),
        ([1,2,3,4,3,2,1], 4),
        ([1,7,2,6,3,5,4], 7),
        ([1,2,3,4,8,9,10], 4),
        ([1,7,3,8,8,9,10], 4),
        ([100, 4, 200, 1, 3, 2], 4),
    ]

    for i, (nums, expected) in enumerate(datas, 1):
        print('-' * 90)
        print('Test {}'.format(i))
        print('nums: {}'.format(nums))
        result = Solution().longestConsecutive(nums)
        print('Result: {}. Expected: {}.'.format(result, result==expected))



