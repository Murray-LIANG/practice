# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        sz = len(intervals)
        if sz == 0:
            return [newInterval]

        newStartPos = None
        l = 0
        r = sz - 1
        while l < r:
            if intervals[l].start > newInterval.start:
                newStartPos = l
                break
            if intervals[r].start < newInterval.start:
                newStartPos = r+1
                break
            m = (l+r) / 2
            if intervals[m].start == newInterval.start:
                newStartPos = m
                break
            elif intervals[m].start > newInterval.start:
                r = m-1
            else:
                l = m+1
        if newStartPos is None:
            if intervals[l].start <newInterval.start:
                newStartPos = l+1
            else:
                newStartPos = l

        newEndPos = None
        l = newStartPos+1
        r = sz - 1
        while l < r:
            if intervals[l].start > newInterval.end:
                newEndPos = l-1
                break
            if intervals[r].start < newInterval.end:
                newEndPos = r
                break
            m = (l+r) / 2
            if intervals[m].start == newInterval.end:
                newEndPos = m
                break
            elif intervals[m].start > newInterval.end:
                r = m-1
            else:
                l = m+1
        newEndPos = l if newEndPos is None else newEndPos

        print(newStartPos, newEndPos)

        result = []
        if newStartPos != 0:
            if newInterval.start > intervals[newStartPos-1].end:
                result += intervals[:newStartPos]
                result.append(newInterval)
            else:
                result += intervals[:newStartPos-1]
                result.append(Interval(intervals[newStartPos-1].start, newInterval.end))
        else:
            result.append(newInterval)
        result += intervals[newEndPos:]
        return result


if __name__ == "__main__":
    cases = [
        [[Interval(1,5)], Interval(1,7)],
        [[Interval(1,3)], Interval(7,10)],
        [[Interval(1,8)], Interval(7,10)],
        [[Interval(1,3),Interval(6,9)], Interval(7,10)],
        [[Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(7,10)],
        [[Interval(2,4),Interval(5,7),Interval(8,10),Interval(11,13)], Interval(3,8)],
    ]

    for case in cases:
        print("case:", " ".join([str(e) for e in case[0]]))
        print("new:", str(case[1]))
        print(" ".join([str(e) for e in Solution().insert(case[0], case[1])]))


        
