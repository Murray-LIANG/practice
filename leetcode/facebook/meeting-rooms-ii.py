# https://leetcode.com/problems/meeting-rooms-ii

"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

import heapq

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int

        There are two solutions here:
        Solution 1:
        Besides record the number of rooms needed, we store the info of the
        number of rooms released. That is, once there is a meeting ending,
        increase the number of rooms released. The released rooms could be used
        for incoming meetings without requesting more rooms.

        Solution 2:
        Use heap to store the meetings on-going on the same time.

        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s = e = 0
        rooms_needed = released = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                # There is new meeting started before last one ends.
                if released > 0:
                    released -= 1
                else:
                    rooms_needed += 1
                s += 1
            else:
                released += 1
                e += 1
        return rooms_needed

    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)

        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in intervals[1:]:
            earliest_end = heapq.heappop()
            if i.start >= earliest_end:
                heapq.heappush(heap, i.end)
            else:
                heapq.heappush(heap, earliest_end)
                heapq.heappush(heap, i.end)
        return len(heap)
