"""
https://leetcode.com/problems/number-of-islands
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        num_islands = 0

        def bfs(row, col):
            from collections import deque
            queue = deque([(row, col)])

            while queue:
                r, c = queue.popleft()
                grid[r][c] = '0'
                for d_r, d_c in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    new_r, new_c = r + d_r, c + d_c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][
                        new_c] == '1':
                        queue.append((new_r, new_c))
            num_islands += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)

        return num_islands
                   