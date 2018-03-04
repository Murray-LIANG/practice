class Solution(object):
    def romeToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        mapping = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
            '': 0
        }

        result = 0
        for i in range(len(s)):
            j = i + 1
            if j == len(s) or mapping[s[i]] >= mapping[s[j]]:
                result += mapping[s[i]]
            else:
                result -= mapping[s[i]]
        return result


if __name__ == '__main__':
    datas = [
        ('MCCXXXIV', 1234),
        ('', 0),
    ]

    for s, expected in datas:
        result = Solution().romeToInt(s)
        print('Rome: {}. Int: {}. Expected: {}'.format(
            s, result, expected == result))

