class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0
        for i in range(32):
            sum = 0
            for n in nums:
                if (abs(n) >> i) & 1 == 1:
                    sum += 1
            sum = sum % 3
            if sum != 0:
                result |= sum << i

        if len(filter(lambda x: x < 0, nums)) % 3:
            return -result
        else:
            return result

if __name__ == '__main__':
    datas = [
        ([1,1,1,2], 2),
        ([1,1,1,3], 3),
        ([5,5,5,3], 3),
        ([1,3,2,3,1,1,3], 2),
        ([-2,-2,1,1,-3,1,-3,-3,-4,-2], -4),
    ]

    for i, (nums, expected) in enumerate(datas, 1):
        print('=' * 60)
        print('Test #{}'.format(i))
        print('nums: {}.'.format(nums))
        result = Solution().singleNumber(nums)
        print('Result: {}. Expected: {}.'.format(result, result==expected))


