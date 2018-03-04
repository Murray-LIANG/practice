class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                nb = self.live_nb(board, m, n, i, j)

                if nb == 3 or (nb == 2 and self.old_state(board, i, j) == 1):
                    board[i][j] += 2

        for i in range(m):
            for j in range(n):
                board[i][j] = self.new_state(board, i, j)

    def old_state(self, board, i, j):
        return board[i][j] & 1

    def new_state(self, board, i, j):
        return board[i][j] >> 1

    def live_nb(self, board, m, n, i, j):
        lives = -self.old_state(board, i, j)

        for x in range(max(i-1, 0), min(i+2, m)):
            for y in range(max(j-1, 0), min(j+2, n)):
                if 0 <= x < m and 0 <= y < n:
                    lives += self.old_state(board, x, y)
        return lives


if __name__ == '__main__':
    datas = [
        ([], []),
        ([[]], [[]]),
        ([[0]], [[0]]),
        ([[1]], [[0]]),
        ([[1,0], [0,1]], [[0,0], [0,0]]),
        ([[1,0,0,1,0],
          [0,1,1,0,1],
          [0,0,0,0,0],
          [1,1,0,1,0]],
         [[0,1,1,1,0],
          [0,1,1,1,0],
          [1,0,0,1,0],
          [0,0,0,0,0]]),
    ]

    for i, (board, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('Board: {}.'.format(board))
        Solution().gameOfLife(board)
        print('Result: {}. Expected: {}. {}.'.format(
            board, expected,
            'PASS' if board==expected else 'FAIL'))
