class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                result.append(abs(num))

        return result


if __name__ == '__main__':
    datas = [
        ([4,3,2,7,8,2,1,3], [2,3]),
        ([4,3,2,2], [2]),
        ([1,1], [1]),
        ([], []),
        ([1], []),
        ([4,3,2,7,8,2,3,1], [2,3]),
    ]

    for i, (nums, expected) in enumerate(datas, 1):
        print('>>> Test {} <<<'.format(i))
        print('Nums: {}.'.format(nums))
        result = Solution().findDuplicates(nums)
        print('Result: {}. Expected:{}. {}.'.format(
            result, expected,
            'PASS' if sorted(result)==sorted(expected) else 'FAIL'))
