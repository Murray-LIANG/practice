# https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 3


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._first(1, n)

    @staticmethod
    def _first(start, end):
        if start == end:
            return start

        mid = (end + start) / 2
        if isBadVersion(mid):
            return Solution._first(start, mid)
        else:
            return Solution._first(mid + 1, end)

    def firstBadVersion_2(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
