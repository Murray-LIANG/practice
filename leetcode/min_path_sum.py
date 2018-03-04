class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        cache = [-1] * n
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1:
                    if j != n - 1:
                        cache[j] = grid[i][j] + cache[j+1]
                    else:
                        cache[j] = grid[i][j]
                else:
                    if j != n - 1:
                        cache[j] = grid[i][j] + min(cache[j], cache[j+1])
                    else:
                        cache[j] = grid[i][j] + cache[j]

        return cache[0]

if __name__ == '__main__':
    cases = [
        [   [2,1,5,3,4,7],
            [2,1,3,4,5,6],
            [2,1,6,5,4,2],
            [2,5,6,5,4,2],
            [2,5,6,4,3,2],
        ]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.minPathSum(case))

