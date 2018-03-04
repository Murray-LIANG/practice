"""
https://leetcode.com/problems/first-bad-version/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        
        left, right = 1, n

        while left < right:
            m = (left + right) / 2
            if isBadVersoin(m):
                right = m
            else:
                left = m + 1
        return left
