class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def checkWord(board, word, indexWord, iBoard, jBoard):
            print('I1', board, word, indexWord, iBoard, jBoard)
            if indexWord == len(word):
                print('O1', board, word, indexWord, iBoard, jBoard)
                return True

            if iBoard >= 0 and iBoard < len(board) \
                    and jBoard >= 0 and jBoard < len(board[0]) \
                    and word[indexWord] == board[iBoard][jBoard]:
                board[iBoard][jBoard] = '*'
                indexWord += 1
                return checkWord(board, word, indexWord, iBoard-1, jBoard) \
                    or checkWord(board, word, indexWord, iBoard+1, jBoard) \
                    or checkWord(board, word, indexWord, iBoard, jBoard-1) \
                    or checkWord(board, word, indexWord, iBoard, jBoard+1)

            print('O2', board, word, indexWord, iBoard, jBoard)
            return False

        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0] and checkWord(board, word, 0, i, j):
                    return True
        return False

if __name__ == '__main__':
    cases = [
        [
            ["C","A","A"],
            ["A","A","A"],
            ["B","C","D"],
            #["A","A","A","A"],
            #["A","A","A","A"],
            #["A","A","A","A"],
            #["S","F","C","S"],
            #["A","D","E","E"]
        ]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        #print(solution.exist(case, "AAAAAAAAAAAA"))
        print(solution.exist(case, "AAB"))

