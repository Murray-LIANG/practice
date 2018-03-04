class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def comb(nums, k, n):
            print(nums, k, n)
            sz = len(nums)

            if k <= 0 or k > 9 or k > sz:
                return []

            if k == 1:
                return [[n]] if n in nums else []

            if k == sz:
                for num in nums:
                    n -= num
                return [nums] if n == 0 else []

            result = []
            for i in range(0, sz):
                subComb = comb(nums[i+1:], k-1, n-nums[i])
                if len(subComb) != 0:
                    result += [[nums[i]] + each for each in subComb]
            return result
        return comb(range(1, 10), k, n)

if __name__ == '__main__':
    cases = [
        [4, 15],
        [3, 12]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.combinationSum3(case[0], case[1]))
