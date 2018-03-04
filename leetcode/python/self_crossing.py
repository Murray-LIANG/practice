class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n = len(x)
        if n < 4:
            return False

        for i in range(3, n):
            # 3 cross 0, 4 cross 1, and so on.
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                print(i)
                print(1)
                return True

            # 4 cross 0, 5 cross 1, and so on.
            if i > 3 and x[i-1] == x[i-3] and x[i-2] <= x[i-4] + x[i]:
                print(i)
                print(2)
                return True

            # 5 cross 0, 6 cross 1, and so on.
            if (i > 4 and x[i-1] <= x[i-3] and x[i-3] - x[i-5] <= x[i-1]
                    and x[i-2] >= x[i-4] and x[i-2] <= x[i-4] + x[i]):
                print(i)
                print(3)
                return True

        return False

if __name__ == '__main__':
    datas = [
        ([], False),
        ([1,2], False),
        ([3,3,3,2,1,1], False),
        ([1,1,2,2,1,1], True),
        ([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1], False),
    ]

    for i, (x, expected) in enumerate(datas, 1):
        print('#' * 60)
        print('Test #{}'.format(i))
        print('x: {}'.format(x))
        result = Solution().isSelfCrossing(x)
        print('Result: {}. Expected: {}.'.format(result, expected == result))

