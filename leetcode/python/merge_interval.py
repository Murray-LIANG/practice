# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[{0}, {1}]".format(self.start, self.end)

def CmpInterval(interval1, interval2):
    return cmp(interval1.start, interval2.start)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        sz = len(intervals)
        if sz == 0:
            return []

        intervals.sort(CmpInterval)
        for e in intervals:
            print(e)

        result = []
        i = 0
        j = 1
        k = i

        while j < sz:
            print(i,k,j)
            if intervals[k].end >= intervals[j].start:
                if intervals[k].end <= intervals[j].end:
                    k = j
                j += 1
            else:
                result.append([intervals[i].start, intervals[k].end])
                i = j
                k = i
                j += 1
        print(i,k,j)
        if i != k:
            result.append([intervals[i].start, intervals[k].end])
        else:
            result.append([intervals[i].start, intervals[i].end])

        return result

if __name__ == '__main__':
    cases = [
        [Interval(5,6),Interval(1,3),Interval(2,4)],
        [Interval(5,6),Interval(1,5),Interval(2,4)],
    ]

    for case in cases:
        print('case:', case)
        print(Solution().merge(case))
        
