# https://leetcode.com/problems/the-skyline-problem

import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        edges = []
        for building in buildings:
            # For the left edge of building, use negative number.
            # This could make sure in the case of two building sharing the same
            # edge, left edge go first than right.
            edges.append((building[0], -building[2]))
            edges.append((building[1], building[2]))

        edges.sort(
            cmp=lambda x, y: x[0] == y[0] and cmp(x[1], y[1]) or cmp(x[0],
                                                                     y[0]))

        heap = []
        heapq.heappush(heap, 0)
        # heapq in python only support min heap. So push the negative height of
        # building into the heap.
        res = []
        prev_height = 0
        for edge in edges:
            if edge[1] < 0:
                heapq.heappush(heap, edge[1])
            else:
                heap.remove(-edge[1])
                heapq.heapify(heap)

            if prev_height != -heap[0]:
                res.append((edge[0], -heap[0]))
                prev_height = -heap[0]
        return res


print(Solution().getSkyline(
    [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(Solution().getSkyline([[0, 2, 3], [2, 5, 3]]))
