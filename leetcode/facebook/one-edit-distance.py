# https://leetcode.com/problems/one-edit-distance

"""
Given two strings S and T, determine if they are both one edit distance apart.
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        # Else s or t is one char longer than the other one
        return abs(len(s) - len(t)) == 1