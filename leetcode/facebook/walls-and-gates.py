"""
https://leetcode.com/problems/walls-and-gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
represent INF as you may assume that the distance to a gate is less than
2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.

        BFS solution.
        """

        if not rooms or not rooms[0]:
            return
        INF = 2 ** 31 - 1
        m, n = len(rooms), len(rooms[0])

        from collections import deque
        queue = deque()

        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            old_row, old_col = queue.popleft()

            for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                row, col = old_row + d[0], old_col + d[1]
                if 0 <= row < m and 0 <= col < n and rooms[row][col] == INF:
                    rooms[row][col] = rooms[old_row][old_col] + 1
                    queue.append((row, col))


