# https://leetcode.com/problems/count-and-say

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def _helper(s):
            res = ''
            s += '0'
            current_num = s[0]
            count = 1
            for num in s[1:]:
                if num == current_num:
                    count += 1
                else:
                    res += str(count) + current_num
                    current_num = num
                    count = 1
            return res

        res = '1'
        for i in range(n-1):
            res = _helper(res)
        return res

print(Solution().countAndSay(1))
print(Solution().countAndSay(8))
