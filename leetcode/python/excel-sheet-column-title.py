# https://leetcode.com/problems/excel-sheet-column-title

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mapping = [chr(ord('A')+num) for num in range(26)]

        res = []
        while n > 0:
            n -= 1
            n, m = divmod(n, 26)
            res.append(mapping[m])

        return ''.join(reversed(res))

print(Solution().convertToTitle(1))
print(Solution().convertToTitle(26))
print(Solution().convertToTitle(27))
print(Solution().convertToTitle(53))



