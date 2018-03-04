class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int

        A DP solution:
        Let T(i, n) is the count of unique BST that is with i as the root, and
        the node number is n.

        C(j) is the count of unique BST that with j nodes.

        T(i, n) = C(i-1) * C(n-i)
        C(n) = SUM{T(i, n)} 1 <= i <= n
             = SUM{C(i-1) * C(n-i)} 1 <= i <= n

        """
        c = [1, 1] # C(0) = C(1) = 1

        for i in range(2, n+1):
            sum = 0
            for j in range(i):
                sum += c[j] * c[i-1-j]
            c.append(sum)

        return c[n]


if __name__ == '__main__':
    datas = [
        (0, 1),
        (1, 1),
        (3, 5),
    ]

    for i, (n, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('n: {}.'.format(n))
        result = Solution().numTrees(n)
        print('Result: {}. Expected:{}. {}.'.format(
            result, expected,
            'PASS' if result==expected else 'FAIL'))
