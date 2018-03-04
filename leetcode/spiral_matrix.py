class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 0:
            return []

        result = []
        for i in range(0, n):
            result.append([0]*n)

        DIRECT = [
            [0, 1], # right
            [1, 0], # down
            [0, -1],# left
            [-1, 0] # up
        ]
        direct = 0
        i = 0
        j = 0

        for cnt in range(1, n*n + 1):
            #print(cnt, i,j)
            #print(result)
            result[i][j] = cnt
            #print(result)

            nextI = i+DIRECT[direct][0]
            nextJ = j+DIRECT[direct][1]
            if nextI < 0 or nextI > n-1 \
                    or nextJ < 0 or nextJ > n-1 \
                    or result[nextI][nextJ] != 0:
                direct += 1
                direct %= 4
            #print(direct)
            i += DIRECT[direct][0]
            j += DIRECT[direct][1]


        return result


if __name__ == '__main__':
    cases = [1,2,3,4,5,6,7]

    for case in cases:
        print(case)
        print(Solution().generateMatrix(case))

