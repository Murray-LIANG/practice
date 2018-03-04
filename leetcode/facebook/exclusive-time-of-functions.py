"""
https://leetcode.com/problems/exclusive-time-of-functions
"""


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        pre_start = None

        for log in logs:
            id, type, time = log.split(':')
            id, time = int(id), int(time)

            if type == 'start':
                if stack:
                    res[stack[-1]] += time - pre_start
                stack.append(id)
                pre_start = time
            else:
                res[stack.pop()] += time - pre_start + 1
                pre_start = time + 1
        return res


print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))