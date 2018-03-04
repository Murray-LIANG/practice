"""
https://leetcode.com/problems/multiply-strings
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def multiply_digit(num, d):
            d = int(d)
            if d == 0: return 0
            res = 0
            for n in num:
                res = res * 10 + d * int(n)
            return res

        res = 0
        for d in num2:
            res = res * 10 + multiply_digit(num1, d)
        return res

