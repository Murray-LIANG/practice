class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Let say we have number a, b, c, d, the length is n.
        After movement, the equal number is Y. So
        Xa + a = Y
        Xb + b = Y
        Xc + c = Y
        Xd + d = Y

        Xa is the moves of number a. Let M is the minimal number of moves.
        Xa + Xb + Xc + Xd = (n - 1) * M = n * Y - Sum{a, b, c, d}
        And M + min{a, b, c, d} = Y.
        Thus, M = Sum{a, b, c, d} - n * min{a, b, c, d}
        """
        return sum(nums) - len(nums) * min(nums) if len(nums) else 0

if __name__ == '__main__':
    datas = [
        ([], 0),
        ([1], 0),
        ([1,2,3], 3),
        ([2,4,6], 6)
    ]

    for i, (nums, expected) in enumerate(datas, 1):
        print('>>>>> Test {}'.format(i))
        print('Nums: {}.'.format(nums))
        result = Solution().minMoves(nums)
        print('Result: {}. Expected: {}.'.format(
            result, result==expected))

