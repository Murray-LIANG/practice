"""
https://leetcode.com/problems/insert-interval
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s, e = newInterval.start, newInterval.end
        left, right = [], []

        for i in intervals:
            if i.end < s:
                left.append(i)
            elif i.start > e:
                right.append(i)
            else:
                s, e = min(s, i.start), max(e, i.end)
        return left + [Interval(s, e)] + right
