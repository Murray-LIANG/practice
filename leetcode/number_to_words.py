class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        numbers = ('_ One Two Three Four Five Six Seven Eight Nine Ten Eleven '
                   'Twelve Thirteen Fourteen Fifteen Sixteen Seventeen '
                   'Eighteen Nineteen').split()
        tens = '_ _ Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()


        def inside_thousand(num):
            if num == 0:
                return []

            if num < 20:
                return [numbers[num]]

            if num < 100:
                i, j = divmod(num, 10)
                return [tens[i]] + inside_thousand(j)

            if num < 1000:
                i, j = divmod(num, 100)
                return [numbers[i], 'Hundred'] + inside_thousand(j)

        def words(num):
            for p, w in ((3, 'Billion'), (2, 'Million'), (1, 'Thousand')):
                tmp = 1000 ** p
                if num >= tmp:
                    i, j = divmod(num, tmp)
                    return inside_thousand(i) + [w] + words(j)

            return inside_thousand(num)

        return ' '.join(words(num))


if __name__ == '__main__':
    data = [
        (0, 'Zero'),
        (20, 'Twenty'),
        (123, 'One Hundred Twenty Three'),
        (1000000010, 'One Billion Ten'),
        (12345, 'Twelve Thousand Three Hundred Forty Five'),
        (1234567, 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'),
        (1000, 'One Thousand'),
    ]

    for num, expected in data:
        message = 'Num: {}.'.format(num)
        result = Solution().numberToWords(num)
        print(message + ' Result: {}. Expected: {}'.format(result,
                                                           result==expected))
