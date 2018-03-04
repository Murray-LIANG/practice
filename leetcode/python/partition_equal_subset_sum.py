class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        0/1 backbag solution:
        Let equal[i][j] is whether the sum of any numbers occurring before
        i(inclusive) is j.
        Then based on pick or not-pick of nums[i], there are two cases for
        equal[i][j].
        case #1: pick nums[i], need to check equal[i-1][j-nums[i]] (j>=nums[i])
        case #2: not pick nums[i], need to check equal[i-1][j].
        Thus, any true of case #1 and #2, equal[i][j] is true.

        1 <= i <= n
        1 <= j <= sum

        """
        if not nums:
            return True

        target = sum(nums)
        if target % 2:
            return False

        target /= 2
        m = len(nums) + 1
        n = target + 1

        """
        # We could save some space.
        equal = [[False] * n] * m
        for i in range(m):
            equal[i][0] = True

        for i in range(1, m):
            for j in range(1, n):
                equal[i][j] = (equal[i-1][j] or
                               equal[i-1][j-nums[i-1]] if j >= nums[i-1]
                               else False)

        print(equal)
        return equal[m-1][target]
        """
        equal = [False] * n
        equal[0] = True

        for i in range(1, m):
            for j in range(n-1, 0, -1):
                equal[j] = (equal[j] or
                            equal[j-nums[i-1]] if j >= nums[i-1]
                            else False)
                print(i, j)
                print(equal)
        return equal[target]
        


if __name__ == '__main__':
    datas = [
        ([], True),
        ([10], False),
        ([3,4], False),
        ([4,4], True),
        ([1,5,11,5], True),
        ([2,2,3,5], True),
    ]

    for i, (nums, expected) in enumerate(datas, 1):
        print('#' * 60)
        print('Test #{}'.format(i))
        print('nums: {}'.format(nums))
        result = Solution().canPartition(nums)
        print('Result: {}. Expected: {}.'.format(result, expected == result))

