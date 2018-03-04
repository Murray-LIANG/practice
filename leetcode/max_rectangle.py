class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])

        heights = [0] * (cols + 1)

        max_area = 0
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            stack = [-1]

            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area


if __name__ == '__main__':
    data = [
        ([], 0),
        (["10100", "10111", "11111", "10010"], 6),
        (["10100", "10111", "11111", "11110"], 8),
    ]

    for matrix, expected in data:
        message = 'Matrix: {}.'.format(matrix)
        result = Solution().maximalRectangle(matrix)
        print(message + ' Result: {}. Expected: {}'.format(result,
                                                           result==expected))
