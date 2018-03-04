"""
https://leetcode.com/problems/arithmetic-slices

Use DP:
dp[i] is the number of arithmetic ending with nums[i].
dp[i+1] = dp[i] + 1 if nums[i+1] - nums[i] == nums[i] - nums[i-1]
          else 0
Take 1,3,5,7,9 as example, dp[4] = dp[3] + 1, because all arithmetic slice
ending with 7 can combine with 9 to a new arithmetic slice ending with 9, and
slice 5,7,9 will be a new one ending with 9.

We can opt to use a variable instead of array dp. And sum them up with going
through the numbers.
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = dp = 0

        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res
