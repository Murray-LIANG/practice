class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1 or numRows >= len(s):
            return s
        result = []
        max_delta = 2 * (numRows - 1)
        for rowNum in range(numRows):
            delta = 2 * (numRows - rowNum - 1)
            start = rowNum
            while True:
                result.append(s[start])
                if delta != 0 and delta != max_delta and start + delta < len(s):
                    result.append(s[start+delta])
                start = start + max_delta
                if start >= len(s):
                    break

        return ''.join(result)


if __name__ == '__main__':
    test_datas = [
        ('PAYPALISHIRING', 0),
        ('PAYPALISHIRING', 1),
        ('PAYPALISHIRING', 2),
        ('PAYPALISHIRING', 3),
        ('PAYPALISHIRING', 4),
        ('PAYPALISHIRING', 5),
        ('PAYPALISHIRING', 14),
        ('A', 2)
    ]

    for data in test_datas:
        print('>>>>> Convert {} in {} rows'.format(data[0], data[1]))
        print(Solution().convert(data[0], data[1]))
        print('')

