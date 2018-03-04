class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int

        The min of max here means if you are with bad lucky every time (guess
        wrong), the minimal money which makes sure you can win.
        Let M(i,j) is the money account of number range i to j.
        M(i,j) = min(i<=k<=j){k + max{M(i,k-1), M(k+1,j)}}
        To let the code cleaner, k==j is pointless, because:
        j-1 + max{M(i,j-2), M(j,j)}
        j   + max{M(i,j-1)}
        k==j-1 costs less then k==j.
        """
        cache = [[0] * (n + 1) for _ in range(n+1)]

        for i in range(n, 0, -1):
            for j in range(i+1, n+1):
                cache[i][j] = min([x + max(cache[i][x-1], cache[x+1][j])
                                   for x in range(i,j)])

        return cache[1][n]


if __name__ == '__main__':
    datas = [
        (3, 2),
        (4, 4),
    ]

    for n, expected in datas:
        result = Solution().getMoneyAmount(n)
        print('n: {}. Result: {}. Expected: {}.'.format(n, result,
                                                        expected == result))
