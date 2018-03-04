"""
https://leetcode.com/problems/string-compression
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = []
        pre_start = 0
        chars.append('$')

        for i in range(1, len(chars)):
            if chars[i] != chars[pre_start]:
                res.append(chars[pre_start] + str(i - pre_start))
                pre_start = i

        return res


print(Solution().compress(['a', 'a', 'a', 'c']))
