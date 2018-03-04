class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        n = len(matrix[0])

        """
        i = 0
        j = n - 1

        while i < j:
            temp = matrix[i][i:j+1]
            for k in range(0, j - i + 1):
                matrix[i][j - k] = matrix[i + k][i]

            for k in range(0, j - i + 1):
                matrix[i + k][i] = matrix[j][i + k]

            for k in range(0, j - i + 1):
                matrix[j][i + k] = matrix[j - k][j]

            for k in range(0, j - i + 1):
                matrix[j - k][j] = temp[0 - (k + 1)]

            i += 1
            j -= 1
        """

        """
        A concise solution:
        For clock-wise rotation, first reverse up and down, then swap
        symmetry.
        1 2 3       7 8 9       7 4 1
        4 5 6  >>>  4 5 6  >>>  8 5 2
        7 8 9       1 2 3       9 6 3

        For anti-clockwise rotation, first reverse right and left, then swap
        symmetry.
        1 2 3       3 2 1       3 6 9
        4 5 6  >>>  6 5 4  >>>  2 5 8
        7 8 9       9 8 7       1 4 7
        """
        matrix.reverse()

        for i in range(0, n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        """
        # Pythonic way.
        matrix[:]= map(list, zip(*matrix[::-1]))
        """


if __name__ == '__main__':
    datas = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
         [[13, 9, 5, 1], [14, 10 , 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]),
    ]

    for i, (matrix, expected) in enumerate(datas, 1):
        print('>>>>> Test {}'.format(i))
        print('Before rotation Matrix: {}.'.format(matrix))
        Solution().rotate(matrix)
        print('After rotation Matrix: {}. Expected: {}.'.format(
            matrix, matrix==expected))

