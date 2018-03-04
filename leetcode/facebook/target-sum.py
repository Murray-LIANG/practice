"""
https://leetcode.com/problems/target-sum
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def dfs(nums, target, total, pos, path, res):
            if pos == len(nums):
                if target == total:
                    res.append(path)
                return

            num = nums[pos]
            dfs(nums, target, total - num, pos + 1, path + '-' + str(num), res)
            dfs(nums, target, total + num, pos + 1, path + '+' + str(num), res)

        def dfs_memo(nums, target, total, pos, memo):
            if (pos, total) in memo:
                return memo[(pos, total)]
            if pos == len(nums):
                if target == total:
                    return set([''])
                return set()

            num = nums[pos]
            minus = dfs_memo(nums, target, total - num, pos + 1, memo)
            res = {('-' + str(num) + each) for each in minus}
            add = dfs_memo(nums, target, total + num, pos + 1, memo)
            res |= {('+' + str(num) + each) for each in add}

            memo[(pos, total)] = res
            return res

        # res = []
        # dfs(nums, S, 0, 0, '', res)
        # return len(res)
        memo = {}
        res = dfs_memo(nums, S, 0, 0, memo)
        return len(res)

    def findTargetSumWays_DP(self, nums, S):
        """

        :param nums:
        :param S:
        :return:

        DP solution:
        Some numbers in nums are positive and others are negative.
        sum(positive) + sum(negative) = S
        sum(positive) - sum(negative) = sum(nums)
        sum(positive) = (S + sum(nums)) / 2
        That is, pick some numbers in nums to be positive, and make their sum
        is (S + sum(nums)) / 2.
        Let dp(i,j) denote that how many time the sum j can be gotten from
        nums[:i]
        Then dp(i,j) = dp(i-1,j) + dp(i-1, j - nums[i-1]) while 1 <= i <= n
        And the initial point dp(0,0) = 1 (because number could be 0), and
        dp(0,j) = 0 (when j != 0).
        """

        def sum_to_target(nums, target):
            # # This uses two dimensional array.
            # n = len(nums)
            # dp = [[False] * (target + 1) for _ in range(n + 1)]
            # dp[0][0] = True
            #
            # for i in range(1, n + 1):
            #     for j in range(0, target + 1):
            #         dp[i][j] += dp[i - 1][j]
            #         if j >= nums[i - 1]:
            #             dp[i][j] += dp[i - 1][j - nums[i - 1]]
            # return dp[n][target]

            # This uses one dimensional array.
            n = len(nums)
            dp = [True] + [False] * (target + 1)
            for i in range(1, n + 1):
                for j in range(target, -1, -1):
                    if j >= nums[i - 1]:
                        dp[j] += dp[j - nums[i - 1]]
            return dp[target]

        target, m = divmod(S + sum(nums), 2)
        if m != 0:
            return 0
        return sum_to_target(nums, target)


print(Solution().findTargetSumWays_DP([1, 1, 1, 1, 1], 3))
print(Solution().findTargetSumWays_DP(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
