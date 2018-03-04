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
            start_map[interval.end] = i
            start_list.append(interval.end)

        start_list.sort()

        for interval in intervals:
            pass

    def min_left(self, start_list, target, l, r):
        if l == r:

        m = (l + r) / 2

        if target == start_list[m]:
            return m

        if target > start_list[m]:
            return self.min_left(start_list, target, m + 1, r)
        else:
            return self.min_left(start_list, target, l, m - 1)

        
    


        
if __name__ == '__main__':
    datas = [
        ([], 1 , 0),
        ([1], 1, 0),
        ([1], 2, 1),
        ([1,1,1], 1, 0),
        ([1,1,1], 2, 3),
        ([1,2,2,1,1], 2, 3),
        ([1,2,2,1,1], 1, 2),
    ]

    for i, (nums, val, expected) in enumerate(datas, 1):
        print('.' * 60)
        print('>>> Test #{}'.format(i))
        print('nums: {}'.format(nums))
        result = Solution().removeElement(nums, val)
        print('Result: {}. Expected: {}......{}'.format(
            result, expected, 'PASS' if result == expected else 'FAIL'))

