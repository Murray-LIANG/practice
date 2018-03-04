"""
https://leetcode.com/problems/remove-invalid-parentheses
"""

def is_valid(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                break
    return count == 0


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        queue = {s}
        while queue:
            any_valid = filter(is_valid, queue)
            if any_valid:
                return list(any_valid)

            queue = {e[:i] + e[i+1:] for i in range(len(e)) for e in queue}
