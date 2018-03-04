# https://leetcode.com/problems/arithmetic-slices-ii-subsequence

"""
Use DP.
Let dp(i,d) denote the total number of arithmetic slices that can be formed
within the list A[0...i] (ending with A[i]). d is the diff between A[i] and its
previous number in the arithmetic slice.

dp(i,d) = sum (dp(j,d) + 1) 0<=j<i
Note the plus 1 here. This is introduced for the calculation of dp(i+1,d),
because in dp(i,d), A[j..i] has two numbers, this slice should not be count
into the ones ending with A[i], but should be count into the ones ending with
A[i+1] or other number after i.
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        res = 0
        dp = []

        for i, i_v in enumerate(A):
            dp.append({})

            for j, j_v in enumerate(A[:i]):
                d = i_v - j_v

                tmp_j = dp[j].get(d, 0)
                res += tmp_j
                dp[i][d] = dp[i].get(d, 0) + tmp_j + 1

        return res


    def numberOfArithmeticSlices_2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict

        res, dp = 0, []
        for i, i_v in enumerate(A):
            dp.append(defaultdict(int))
            for j, j_v in enumerate(A[:i]):
                d = i_v - j_v
                # think like this:
                # dp is the number of slice with length >= 2
                # dp[i][d] += 1 -> adding one for (A[j],A[i]) is a new length-2
                # slice.
                # dp[i][d] += dp[j][d] -> adding dp[j][d] for all slices like
                # (A[x],A[j],A[i]) with length >= 3. And we only record the
                # number of these slices for final result.
                dp[i][d] += dp[j][d] + 1
                res += dp[j][d]
        return res

print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))
print(Solution().numberOfArithmeticSlices_2([2, 4, 6, 8, 10]))
print(Solution().numberOfArithmeticSlices_2([2, 2, 3, 4]))
