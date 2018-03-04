# https://leetcode.com/problems/powx-n

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        if n % 2 == 0:
            return Solution().myPow(x * x, n / 2)
        else:
            return x * Solution().myPow(x * x, n / 2)

print(Solution().myPow(3.89707, 2))
print(3.89707 ** 2)


