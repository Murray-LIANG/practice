class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        ugly = [1]

        i2 = i3 = i5 = 0

        for _ in range(n-1):
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            ugly.append(umin)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1

        return ugly[-1]


if __name__ == '__main__':
    datas = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (10, 12),
    ]

    for i, (n, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('n: {}.'.format(n))
        result = Solution().nthUglyNumber(n)
        print('Result: {}. Expected: {}. {}.'.format(
            result, expected,
            'PASS' if result==expected else 'FAIL'))
