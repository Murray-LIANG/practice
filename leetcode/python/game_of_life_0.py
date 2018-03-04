class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return

        for i in range(0, m):
            for j in range(0, n):
                sum_1s = 0
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if x < 0 or y < 0 or x >= m or y >= n or (x == i and y == j):
                            continue
                        sum_1s += board[x][y] % 2
                if board[i][j] == 0:
                    if sum_1s == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 0
                elif board[i][j] == 1:
                    if sum_1s < 2 or sums_1s > 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] < 2:
                    board[i][j] = 0
                else:
                    board[i][j] = 1


if __name__ == '__main__':
    cases = [
        [
            [1,0,1],
            [0,0,1],
            [1,1,0],
            [0,1,0],
        ]
    ]

    for case in cases:
        print(case)
        print(Solution().gameOfLife(case))

