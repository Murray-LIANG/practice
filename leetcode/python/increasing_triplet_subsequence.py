class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1 = 2 ** 32
        n2 = n1

        for n in nums:
            if n <= n1:
                n1 = n
            elif n <= n2:
                n2 = n
            else:
                return True

        return False


if __name__ == '__main__':
    datas = [
        ([5], False),
        ([1,2], False),
        ([1,2,3], True),
        ([1,1,1], False),
        ([5,4,3,2,1], False),
        ([5,1,4,2,3], True),
    ]

    for i, (nums, expected) in enumerate(datas, 1):
        print('#' * 60)
        print('Test #{}'.format(i))
        print('nums: {}'.format(nums))
        result = Solution().increasingTriplet(nums)
        print('Result: {}. Expected: {}.'.format(result, expected == result))

