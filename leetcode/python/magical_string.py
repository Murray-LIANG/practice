class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0

        if n < 4:
            return 1

        array = [1, 2, 2]
        num_to_fill = 1

        result =  1

        for i in range(2, n):
            if array[i] == 1:
                result += 1
            array += [num_to_fill] * array[i]
            num_to_fill ^= 3

        return result

if __name__ == '__main__':
    datas = [
        (0, 0),
        (1, 1),
        (3, 1),
        (4, 2),
        (6, 3),
    ]

    for i, (n, expected) in enumerate(datas, 1):
        print('-' * 90)
        print('Test {}'.format(i))
        print('n: {}'.format(n))
        result = Solution().magicalString(n)
        print('Result: {}. Expected: {}.'.format(result, result==expected))



