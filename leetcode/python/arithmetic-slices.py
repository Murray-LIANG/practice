# https://leetcode.com/problems/arithmetic-slices

"""
Consider this case, 3,5,7,9,10
For list [3,5], number of arithmetic slices ending with 5 is 0.
Then check [3,5,7], because the diff of 3 and 5 is same as the diff of 5,7,
number of arithmetic slices ending with 7 is 0+1.
Then [3,5,7,9], number of arithmetic slices ending with 9 is 0+1+1.

Then [3,5,7,9,10], because the diff of 9 and 10 is not same any more,
number of arithmetic slices ending with 10 is back to 0.


"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                count += 1
                res += count
            else:
                count = 0

        return res
