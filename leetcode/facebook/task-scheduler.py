# https://leetcode.com/problems/task-scheduler

from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int

        There are two cases:
        1. There is no idle interval between any two tasks.
        2. There is.
        For case 1, the result is number of tasks.
        For case 2, use the task with most frequency to split all tasks into
        (k-1) chunks (k is the Count(A)), like:
        AXXXAXXXAXXXA...
        Under this situation, the result is (Count(A)-1) * (n+1) + len(A...)
        And schedule the meetings in case 2? The strategy is always choosing
        the chunk which has least meetings.
        """

        count = Counter(tasks)

        count_num = sorted(count.values(), reverse=True)

        return max(
            len(tasks),
            (count_num[0] - 1) * (n + 1) + count_num.count(count_num[0]))


print(Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2))
