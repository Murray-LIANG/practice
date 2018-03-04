# https://leetcode.com/problems/number-of-islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        grid = [list(row) for row in grid]
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0':
                    continue
                res += 1

                queue = [(row, col)]
                grid[row][col] = '0'
                while queue:
                    cur_row, cur_col = queue[0]
                    queue = queue[1:]
                    for dir in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                        new_row = cur_row + dir[0]
                        new_col = cur_col + dir[1]
                        if 0 <= new_row < m and 0 <= new_col < n \
                                and grid[new_row][new_col] == '1':
                            grid[new_row][new_col] = '0'
                            queue.append((new_row, new_col))

        return res


print(Solution().numIslands(["11110", "11010", "11000", "00000"]))
print(Solution().numIslands(["1011101"]))
print(Solution().numIslands(["111", "010", "111"]))
