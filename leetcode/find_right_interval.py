# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """

        start_map = {}
        start_list = []
        for i, interval in enumerate(intervals):
            start_map[interval.start] = i
            start_list.append(interval.start)

        start_list.sort()

        result = []
        for interval in intervals:
            min_left = self.min_left(start_list, interval.end,
                                     0, len(start_list) - 1)

            result.append(-1 if min_left == -1 else start_map[min_left])
        return result


    def min_left(self, start_list, target, l, r):
        if l == r:
            if target > start_list[r]:
                if r == len(start_list) - 1:
                    return -1
                else:
                    return start_list[r+1]
            else:
                return start_list[r]

        m = (l + r) / 2

        if target == start_list[m]:
            return start_list[m]

        if target > start_list[m]:
            return self.min_left(start_list, target, m + 1, r)
        else:
            return self.min_left(start_list, target, l, m - 1)


if __name__ == '__main__':
    datas = [
        ([[3,4],[2,3],[1,2]], [-1,0,1]),
        ([[1,4],[2,3],[3,4]], [-1,2,-1]),
        ([[4,5],[2,3],[1,2]], [-1,0,1]),
    ]

    for i, (intervals, expected) in enumerate(datas, 1):
        print('.' * 60)
        print('>>> Test #{}'.format(i))
        print('intervals: {}'.format(intervals))
        intervals = [Interval(l[0], l[1]) for l in intervals]

        result = Solution().findRightInterval(intervals)
        print('Result: {}. Expected: {}......{}'.format(
            result, expected, 'PASS' if result == expected else 'FAIL'))

