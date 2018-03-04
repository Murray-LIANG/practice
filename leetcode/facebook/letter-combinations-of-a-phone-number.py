"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv',
               'wxyz']

        res = [[]]
        for digit in digits:
            res = [each.append(ch) for each in res for ch in map[int(digit)]]
        return [] if not res[0] else res

print(Solution().letterCombinations('233'))
